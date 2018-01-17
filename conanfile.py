from conans import ConanFile, Meson


class RangConan(ConanFile):
    name = "rang"
    version = "3.0.0"
    license = "The Unlicense"
    url = "https://github.com/agauniyal/rang"
    description = "A Minimal, Header only Modern c++ library for colors in your terminal"
    generators = "pkg_config"
    build_requires = "doctest/1.2.6@bincrafters/stable"

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()

    def package(self):
        self.copy("*.hpp")

    def package_id(self):
        self.info.header_only()
