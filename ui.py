
#class UI():
   # # function UI(tape_catalog, runner, memory, autoexec) {
    # def __init__ (self,tape_catalog, runner, memory, autoexec)
        # self.tape_catalog = tape_catalog;
        # self.runner = runner;
        # self.memory = memory;
        # self.autoexec = autoexec;

        # #self.canvas = document.getElementById("canvas");
        # #self.panel = document.getElementById("back");
        # #self.fullscreen_panel = document.getElementById("fullscreen_panel");
        
        # #this.screenshot_name = "rk86-screen";
        # #this.screenshot_count = 1;

  # #self.screenshot_name = "rk86-screen";
  # #self.screenshot_count = 1;
def parse_rk86_binary (name):
    f=open('files/'+name, mode='rb')
    file_ = {}
    file_['image']=f.read()
   
    file_['name'] = 'chars'
    file_['size'] = len(file_['image'])
    file_['start']=0
    file_['end']=file_['size']
    return file_
       
       
       
       
