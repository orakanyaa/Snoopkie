import arcade
from models import Monster,Snoopy

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class MonsterWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Monster Keeper")
        self.background = arcade.load_texture("images/homeee.png")  
        self.Snoopy = Snoopy("images/snoopy.png",0.75)
        self.Monster = Monster("images/cookiemon.png", 0.5, self.Snoopy)
        
    def on_key_release(self, key, modifiers):
        self.Snoopy.on_key_release(key, modifiers)
    
    def on_key_press(self, key, modifiers):
        self.Snoopy.on_key_press(key, modifiers)
        if key == arcade.key.R:
            if self.Monster.score < 0:
                self.Snoopy = Snoopy("images/snoopy.png",0.75)
                self.Monster = Monster("images/cookiemon.png", 0.5, self.Snoopy)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.Monster.on_draw()
        self.Snoopy.draw()
        if self.Monster.score < 0 :
            arcade.draw_text("GAME OVER", 200, 300, arcade.color.BLACK, 50)
            arcade.draw_text("Press R to restart", 222, 250 , arcade.color.BLACK, 30)
        else :
            arcade.draw_text("Score : "+str(self.Monster.score), 10, 650, arcade.color.WHITE, 30)

    def update(self, delta):
        self.Monster.update()
        self.Snoopy.update()
        if self.Monster.score < 0 :
            arcade.draw_text("GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.BLACK, 50)
            arcade.draw_text("Press R to restart", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2+200 , arcade.color.BLACK, 30)
        else :
            arcade.draw_text("Score : "+str(self.Monster.score), 600, 600, arcade.color.WHITE, 30)

def main():
    window = MonsterWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
