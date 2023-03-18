from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import get_color_from_hex



from kivy.utils import platform

from kivy.utils import get_hex_from_color, platform


def change_statusbar_color(statuscolor, icons_color="Light"):

    if platform != "android":
        return

    from android.runnable import run_on_ui_thread
    from jnius import autoclass

    Color = autoclass("android.graphics.Color")
    WindowManager = autoclass("android.view.WindowManager$LayoutParams")
    activity = autoclass("org.kivy.android.PythonActivity").mActivity
    View = autoclass("android.view.View")

    def statusbar(*args):
        color = get_hex_from_color(statuscolor)[:7]
        window = activity.getWindow()

        if icons_color == "Dark":
            window.getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR
            )
        elif icons_color == "Light":
            window.getDecorView().setSystemUiVisibility(0)

        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color))
        window.setNavigationBarColor(Color.parseColor(color))

    status = run_on_ui_thread(statusbar)

    return status()
    
change_statusbar_color((1,0,0,1))

kv = """
#:import OpacityScrollEffect  kivy.effects.opacityscroll.OpacityScrollEffect
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDScreen:
	MDBoxLayout:
		size_hint:1,1
		orientation:"vertical"
		minimum_height:1
		#MDBoxLayout:
#			orientation:"vertical"
#			size_hint:1,None
#			height:"70dp"
		MDBottomNavigation:
			tab_header:True
			#panel_color: "#673AB760"
			text_color_normal: 1, 0, 1, 1
        	text_color_active: "lightgrey"
        	selected_color_background:0,0,0,1
        	use_text:False
        	set_bars_color:True
			MDBottomNavigationItem:
				icon: 'twitter'
				text:"home"
				badge_icon: "numeric-5"
				name: "screen 1"
				MDGridLayout:
	            	cols:1
					md_bg_color:.9,.9,.9,1
					ScrollView:
						effect_cls:"OpacityScrollEffect"
						size_hint:1,1
						do_scroll_y: True
						MDGridLayout:
							cols:1
							size_hint:1,None
							height:self.minimum_height
							spacing:"10dp"
							padding:"10dp"
							MDCard:
								size_hint:1,None
								height:"240dp"
								md_bg_color:1,1,1,1
									
							MDCard:
								text:"1"
								size_hint:1,None
								height:"240dp"
								md_bg_color:1,1,1,1
									
							MDCard:
								text:"1"
								size_hint:1,None
								height:"240dp"
								md_bg_color:1,1,1,1
									
							MDCard:
								text:"1"
								size_hint:1,None
								height:"240dp"
								md_bg_color:1,1,1,1  
			MDBottomNavigationItem:
				name: "screen 2"
				icon: 'twitter'
				badge_icon: "numeric-5"
				MDLabel:
					text:"hello 2"
			MDBottomNavigationItem:
				name: "screen 3"
				icon: 'twitter'
				badge_icon: "numeric-5"
				MDLabel:
					text:"hello 3"
			MDBottomNavigationItem:
				name: "screen 4"
				icon: 'account'
				badge_icon: ""
				MDLabel:
					text:"hello 4"
						
"""


class MyApp(MDApp):
	def on_start(self):
		self.theme_cls.primary_palette = "DeepPurple"
	def build(self):
		return Builder.load_string(kv)

if __name__ == "__main__":
	MyApp().run()
