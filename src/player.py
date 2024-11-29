import objects
import weapon


class Player(objects.GameObject):
    x = 0
    y = 0
    speed = 5
    name = 'hero'
        
    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed
        
    def shoot(self, name='laser'):
        bullet = weapon.Bullet(x=self.x, y=self.y, filename=name)
        if bullet.sound:
            bullet.sound.set_volume(0.03)
            bullet.sound.play()
        return bullet
