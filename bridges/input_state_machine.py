
class InputStateMachine:
    def __init__(self, raw):
        self.s = "STILL_NOT_PRESSED"
        self.f = "NOT_PRESSED"
        self.cooldown = 30
        self.cooldownCounter = 0
        self.rawState = raw
    
    def update(self):
        cs = self.rawState()
        
        #update cycle state
        if self.s == "JUST_PRESSED":
            if cs:
                self.s = "STILL_PRESSED"
            else:
                self.s = "JUST_NOT_PRESSED"
        elif self.s == "STILL_PRESSED":
            if cs:
                self.s = "STILL_PRESSED"
            else:
                self.s = "JUST_NOT_PRESSED"
        elif self.s == "JUST_NOT_PRESSED":
            if cs:
                self.s = "JUST_PRESSED"
            else:
                self.s = "STILL_NOT_PRESSED"
        elif self.s == "STILL_NOT_PRESSED":
            if cs:
                self.s = "JUST_PRESSED"
            else:
                self.s = "STILL_NOT_PRESSED"
        
        #update firestate
        if self.f == "FIRE":
            if cs:
                self.f = "COOLDOWN"
                self.cooldownCounter = self.cooldown
            else:
                self.f = "NOT_PRESSED"
        elif self.f == "COOLDOWN":
            if cs:
                self.cooldownCounter = self.cooldownCounter - 1
                if self.cooldownCounter == 0:
                    self.f = "FIRE"
            else:
                self.f = "NOT_PRESSED"
        elif self.f == "NOT_PRESSED":
            if cs:
                self.f = "FIRE"
            else:
                self.f = "NOT_PRESSED"
    
    def just_pressed(self):
        return self.s == "JUST_PRESSED"
    
    def still_pressed(self):
        return self.s == "STILL_PRESSED"
    
    def just_not_pressed(self):
        return self.s == "JUST_NOT_PRESSED"
    
    def still_not_pressed(self):
        return self.s == "STILL_NOT_PRESSED"
    
    def set_fire_cooldown(self,  c: int):
        if c <= 0:
            raise "cooldown must be positive"
        
        self.cooldown = c;
    
    def fire(self):
        return self.f == "FIRE"

