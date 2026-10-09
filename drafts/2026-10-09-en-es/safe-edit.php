<?php
// Server-only MediaWiki maintenance command with native compare-and-swap protection.
use MediaWiki\CommentStore\CommentStoreComment;
use MediaWiki\Content\ContentHandler;
use MediaWiki\Revision\SlotRecord;
use MediaWiki\Title\Title;
use MediaWiki\User\User;
require_once '/applis/wiki/www/maintenance/Maintenance.php';
class WikiNrSafeEdit extends Maintenance {
    public function __construct() {
        parent::__construct();
        $this->addOption('base', 'Expected current revision, or zero for a new page', true, true);
        $this->addOption('dry-run', 'Check revision without writing', false, false);
        $this->addArg('title', 'Exact page title');
    }
    public function execute() {
        $base = $this->getOption('base');
        if (!ctype_digit((string)$base)) { $this->fatalError('Invalid base revision'); }
        $title = Title::newFromText($this->getArg(0));
        if (!$title || $title->getNamespace() !== NS_MAIN) { $this->fatalError('Invalid article title'); }
        $user = User::newSystemUser(User::MAINTENANCE_SCRIPT_USER, ['steal' => true]);
        $page = $this->getServiceContainer()->getWikiPageFactory()->newFromTitle($title);
        $updater = $page->newPageUpdater($user);
        // Establishes the CAS token; saveRevision also rejects later concurrent edits.
        if ($updater->hasEditConflict((int)$base)) { $this->fatalError('Revision conflict; no page was changed'); }
        if ($this->hasOption('dry-run')) { $this->output("Revision check OK\n"); return true; }
        $text = $this->getStdin(Maintenance::STDIN_ALL);
        if (trim($text) === '') { $this->fatalError('Empty content refused'); }
        $updater->setContent(SlotRecord::MAIN, ContentHandler::makeContent($text, $title));
        $updater->saveRevision(CommentStoreComment::newUnsavedComment(
            'Translate and clarify responsible IT guidance; retain sources and language links'
        ), (int)$base === 0 ? EDIT_NEW : EDIT_UPDATE);
        if (!$updater->getStatus()->isOK()) { $this->fatalError((string)$updater->getStatus()); }
        $this->output("Saved with revision conflict protection\n");
        return true;
    }
}
$maintClass = WikiNrSafeEdit::class;
require_once RUN_MAINTENANCE_IF_MAIN;
