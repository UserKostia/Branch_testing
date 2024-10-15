from fastapi_babel import Babel, BabelConfigs, _
# from fastapi_babel.core import _

configs = BabelConfigs(
    ROOT_DIR=__file__,
    BABEL_DEFAULT_LOCALE="en",
    BABEL_TRANSLATION_DIRECTORY="lang",
)
babel = Babel(configs=configs)


def main():
    babel.locale = "en"
    en_text = _("Hello World")
    print(en_text)

    print("---------- HELLLLLOOOO --------------------")

    babel.locale = "fa"
    fa_text = _("Hello World")
    print(fa_text)


if __name__ == "__main__":
    main()
