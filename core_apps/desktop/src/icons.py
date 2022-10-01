from tkfontawesome import icon_to_image

class Icons:
    def __init__(self):
        self.TITANIUM_ICON = icon_to_image("home", scale_to_height=16)
        self.SETTINGS_ICON = icon_to_image("cog", scale_to_height=16)

        self.CODE_TOOLS_ICON = icon_to_image("code", scale_to_height=16)
        self.TRANSCRIPT_ICON = icon_to_image("newspaper", scale_to_height=16)
        self.PROJECT_EXPLORER_ICON = icon_to_image("project-diagram", scale_to_height=16)
        self.CODE_YARD_ICON = icon_to_image("atom", scale_to_height=16)

        self.SYSTEM_ICON = icon_to_image("boxes", scale_to_height=16)
        self.TERMINAL_ICON = icon_to_image("terminal", scale_to_height=16)
        self.FINDER_ICON = icon_to_image("search", scale_to_height=16)
        self.SCREENSHOT_ICON = icon_to_image("camera", scale_to_height=16)
        self.SCREEN_RECORDER_ICON = icon_to_image("camera", scale_to_height=16)

        self.HELP_ICON = icon_to_image("info", scale_to_height=16)
        self.TUTORIAL_ICON = icon_to_image("info", scale_to_height=16)
        self.ZEAL_ICON = icon_to_image("book", scale_to_height=16)

        self.OTHER_ICON = icon_to_image("box", scale_to_height=16)