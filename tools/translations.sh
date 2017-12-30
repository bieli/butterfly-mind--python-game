xgettext -d translations -o locale/pl_PL/LC_MESSAGES/translations.po font1.py
cd locale/pl_PL/LC_MESSAGES/
msgfmt -o translations.mo translations.po
cd ../../..
