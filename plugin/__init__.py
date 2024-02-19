import gettext
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

PluginLanguageDomain = "YampMusicPlayer"
PluginLanguagePath = "Extensions/YampMusicPlayer/locale"


def localeInit():
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
		print(f"[Yamp] Fallback to default Enigma2 Translation for '{txt}'")
		t = gettext.gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)
