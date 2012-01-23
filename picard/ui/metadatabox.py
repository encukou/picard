# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2004 Robert Kaye
# Copyright (C) 2006 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from PyQt4 import QtCore, QtGui
from picard.util import format_time
from picard.album import Album
from picard.file import File

class MetadataBox(QtGui.QGroupBox):

    def __init__(self, parent, title, read_only=False):
        QtGui.QGroupBox.__init__(self, title)
        self.metadata = None
        self.read_only = read_only

        from picard.ui.ui_metadata import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.title.setReadOnly(self.read_only)
        self.ui.artist.setReadOnly(self.read_only)
        self.ui.album.setReadOnly(self.read_only)
        self.ui.tracknumber.setReadOnly(self.read_only)
        self.ui.date.setReadOnly(self.read_only)

        self.connect(self.ui.lookup, QtCore.SIGNAL("clicked()"), self.lookup)
        self.connect(self.ui.title, QtCore.SIGNAL("textEdited(QString)"), self.update_metadata_title)
        self.connect(self.ui.album, QtCore.SIGNAL("textEdited(QString)"), self.update_metadata_album)
        self.connect(self.ui.artist, QtCore.SIGNAL("textEdited(QString)"), self.update_metadata_artist)
        self.connect(self.ui.tracknumber, QtCore.SIGNAL("textEdited(QString)"), self.update_metadata_tracknum)
        self.connect(self.ui.date, QtCore.SIGNAL("textEdited(QString)"), self.update_metadata_date)

        self.disable()

    def enable(self, is_album):
        if not is_album:
            self.ui.title.setDisabled(False)
            self.ui.tracknumber.setDisabled(False)
        else:
            self.ui.title.setDisabled(True)
            self.ui.tracknumber.setDisabled(True)
        self.ui.artist.setDisabled(False)
        self.ui.album.setDisabled(False)
        self.ui.length.setDisabled(False)
        self.ui.date.setDisabled(False)
        self.ui.lookup.setDisabled(False)

    def disable(self):
        self.ui.title.setDisabled(True)
        self.ui.artist.setDisabled(True)
        self.ui.album.setDisabled(True)
        self.ui.tracknumber.setDisabled(True)
        self.ui.length.setDisabled(True)
        self.ui.date.setDisabled(True)
        self.ui.lookup.setDisabled(True)

    def clear(self):
        self.ui.title.clear()
        self.ui.artist.clear()
        self.ui.album.clear()
        self.ui.length.clear()
        self.ui.tracknumber.clear()
        self.ui.date.clear()

    def set_metadata(self, metadata, is_album=False, obj=None):
        self.metadata = metadata
        self.obj = obj
        if metadata:
            if is_album:
                self.setText(self.ui.album, metadata['album'])
                self.ui.title.clear()
                self.ui.tracknumber.clear()
            else:
                self.setText(self.ui.album, metadata['album'])
                self.setText(self.ui.title, metadata['title'])
                self.setText(self.ui.tracknumber, metadata['tracknumber'])
            self.setText(self.ui.artist, metadata['artist'])
            self.setText(self.ui.length, format_time(metadata.length))
            self.setText(self.ui.date, metadata['date'])
            self.enable(is_album)
        else:
            self.clear()
            self.disable()

    def setText(self, textbox, text):
        """Helper for setting the text of a textbox.
        If the original text is the same, do nothing
        """
        # Needed to avoid the cursor jumping to the end of the box
        # with every keystroke while editing
        if textbox.text() != text:
            textbox.setText(text)

    def lookup(self):
        """Tell the tagger to lookup the metadata."""
        self.tagger.lookup(self.metadata)

    def _update_metadata(self, name, text, whole_album=False):
        if self.metadata and isinstance(self.obj, File):
            self.metadata[name] = unicode(text)
            self.obj.update()
        elif whole_album and self.metadata and isinstance(self.obj, Album):
            self.metadata[name] = unicode(text)
            self.obj.update()
            for track in self.obj.tracks:
                if len(track.linked_files) == 1:
                    track.linked_files[0].metadata[name] = unicode(text)
                    track.linked_files[0].update()

    def update_metadata_title(self, text):
        self._update_metadata('title', text)

    def update_metadata_album(self, text):
        self._update_metadata('album', text, True)

    def update_metadata_artist(self, text):
        self._update_metadata('artist', text, True)

    def update_metadata_tracknum(self, text):
        self._update_metadata('tracknumber', text)

    def update_metadata_date(self, text):
        self._update_metadata('date', text, True)
