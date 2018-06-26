class Runner(cpu):
    cpu = cpu;
    paused = false
    tracer = null
    visualizer = null

    FREQ = 2100000
    TICK_PER_MS = FREQ / 100

    cpu.jump(0xf800)
    def.execute(self):
        if (self.paused):
            ticks = 0
        while (ticks < TICK_PER_MS):
            if (this.tracer):
                #this.tracer(this)
                if (self.paused) break
        
                ticks += self.cpu.instruction()
                if (self.visualizer):
                    self.visualizer.hit(self.cpu.memory.read_raw(self.cpu.pc))
                    
             #runner_self = this;
             #window.setTimeout(function() { runner_self.execute(); }, 10);
             
    def pause(self):
        self.paused=True
        
    def resume(self):
        self.paused=False