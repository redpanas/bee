PREFIX ?= /usr/local
DESTDIR ?=

.PHONY: install uninstall test

install:
	install -Dm755 bee "$(DESTDIR)$(PREFIX)/bin/bee"
	install -Dm644 LICENSE "$(DESTDIR)$(PREFIX)/share/licenses/bee/LICENSE"
	install -Dm644 README.md "$(DESTDIR)$(PREFIX)/share/doc/bee/README.md"

uninstall:
	rm -f "$(DESTDIR)$(PREFIX)/bin/bee"
	rm -rf "$(DESTDIR)$(PREFIX)/share/licenses/bee" "$(DESTDIR)$(PREFIX)/share/doc/bee"

test:
	sh -n bee
	./bee --version | grep -qx 'bee 1.0.0'
	./bee --help | grep -q '^Usage:'
