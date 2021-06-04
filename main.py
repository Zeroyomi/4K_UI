import os, sys
import kivy
#kivy.require('1.0.6') # replace with your current kivy version !
from kivy.resources import resource_add_path, resource_find
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ListProperty
import time
import serial

kv = Builder.load_file('./smart.kv')


class MyLayout(TabbedPanel): #inherit TabbedPanel
   gamvalue = [4,1,6]
   ee = ListProperty([128,128,2048,2048,24,4])
#----------------------------basic---------------------------------------     
   def btn_wb(self):
      s.write("wb\r".encode("utf-8"))
      s.flush()
      self.ids.wb_label.text = "Manual white Balance done!"
   def btn_awb(self):
      s.write("awb auto\r".encode("utf-8"))
      s.flush()
      self.ids.wb_label.text = "Standard auto White Balance mode"
   def btn_awb_flu(self):
      s.write("awb flu\r".encode("utf-8"))
      s.flush()
      self.ids.wb_label.text = "Auto-Fluorescent mode"
   def slide_lbshift(self, *args):
      try:
         s.write(("lb "+str(args[1]) + "\r").encode("utf-8"))
      except:
         print('lbshift error')

   def switch_cc(self, switchValue):
      if (switchValue == False):
         try:
            s.write("cc off\r".encode("utf-8"))
         except:
            print('cc deactive error')   
            
      else:
         try:
            s.write("cc on\r".encode("utf-8"))
         except:
            print('cc active error')

   def switch_flip(self, switchValue):
      if (switchValue == False):
         try:
            s.write("hflip\r".encode("utf-8"))
         except:
            print('gamma deactive error')   
            
      else:
         try:
            s.write("hflip\r".encode("utf-8"))
         except:
            print('flip active error')            
#----------------------------ae---------------------------------------      
   def slide_ae(self, *args):
      try:
         brightness = str(int(args[1]))
         #print(brightness)
         #self.ids.brightness.text = str(int(args[1]))
         brightness = "target " + brightness + " 65535\r"
         #print(brightness)
         s.write(brightness.encode("utf-8"))
      except:
         print('brightness error')

   def slide_lshd(self, *args):
      try:
         lshd = str(int(args[1]))
         lshd = "lshd " + lshd + "\r"
         #print(lshd)
         s.write(lshd.encode("utf-8"))
      except:
         print('lshd error')

   def switch_lshd(self, switchValue):
      if (switchValue == False):
         try:
            s.write("lshd off\r".encode("utf-8"))
         except:
            print('lshd deactive error')   
            
      else:
         try:
            s.write("lshd on\r".encode("utf-8"))
         except:
            print('lshd active error')         
#----------------------------color--------------------------------------
#----------------------------magenta--------------------------------------
   def slide_m_h(self, *args):
      try:
         s.write(("umm " + "mag " + str(args[1]) + " " + str(self.ids.s_m_s.value) + " " + str(self.ids.s_m_d.value) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_m_s(self, *args):
      try:
         s.write(("umm " + "mag " + str(self.ids.s_m_h.value) + " " + str(args[1]) + " " + str(self.ids.s_m_d.value) + "\r" ).encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_m_d(self, *args):
      try:
         s.write(("umm " + "mag " + str(self.ids.s_m_h.value) + " " + str(self.ids.s_m_s.value) + " " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
#----------------------------red--------------------------------------
   def slide_r_h(self, *args):
      try:
         s.write(("umm " + "red " + str(args[1]) + " " + str(self.ids.s_r_s.value) + " " + str(self.ids.s_r_d.value) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_r_s(self, *args):
      try:
         s.write(("umm " + "red " + str(self.ids.s_r_h.value) + " " + str(args[1]) + " " + str(self.ids.s_r_d.value) + "\r" ).encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_r_d(self, *args):
      try:
         s.write(("umm " + "red " + str(self.ids.s_r_h.value) + " " + str(self.ids.s_r_s.value) + " " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
         
#----------------------------yellow--------------------------------------
   def slide_y_h(self, *args):
      try:
         s.write(("umm " + "yellow " + str(args[1]) + " " + str(self.ids.s_y_s.value) + " " + str(self.ids.s_y_d.value) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_y_s(self, *args):
      try:
         s.write(("umm " + "yellow " + str(self.ids.s_y_h.value) + " " + str(args[1]) + " " + str(self.ids.s_y_d.value) + "\r" ).encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_y_d(self, *args):
      try:
         s.write(("umm " + "yellow " + str(self.ids.s_y_h.value) + " " + str(self.ids.s_y_s.value) + " " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')         
   
#----------------------------green--------------------------------------
   def slide_g_h(self, *args):
      try:
         s.write(("umm " + "green " + str(args[1]) + " " + str(self.ids.s_g_s.value) + " " + str(self.ids.s_g_d.value) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_g_s(self, *args):
      try:
         s.write(("umm " + "green " + str(self.ids.s_g_h.value) + " " + str(args[1]) + " " + str(self.ids.s_g_d.value) + "\r" ).encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_g_d(self, *args):
      try:
         s.write(("umm " + "green " + str(self.ids.s_g_h.value) + " " + str(self.ids.s_g_s.value) + " " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
         
#----------------------------cyan--------------------------------------
   def slide_c_h(self, *args):
      try:
         s.write(("umm " + "cyan " + str(args[1]) + " " + str(self.ids.s_c_s.value) + " " + str(self.ids.s_c_d.value) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_c_s(self, *args):
      try:
         s.write(("umm " + "cyan " + str(self.ids.s_c_h.value) + " " + str(args[1]) + " " + str(self.ids.s_c_d.value) + "\r" ).encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_c_d(self, *args):
      try:
         s.write(("umm " + "cyan " + str(self.ids.s_c_h.value) + " " + str(self.ids.s_c_s.value) + " " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')

#----------------------------blue--------------------------------------
   def slide_b_h(self, *args):
      try:
         s.write(("umm " + "blue " + str(args[1]) + " " + str(self.ids.s_b_s.value) + " " + str(self.ids.s_b_d.value) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_b_s(self, *args):
      try:
         s.write(("umm " + "blue " + str(self.ids.s_b_h.value) + " " + str(args[1]) + " " + str(self.ids.s_b_d.value) + "\r" ).encode("utf-8"))
         s.flush()
      except:
         print('color error')
   def slide_b_d(self, *args):
      try:
         s.write(("umm " + "blue " + str(self.ids.s_b_h.value) + " " + str(self.ids.s_b_s.value) + " " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('color error')
#----------------------------ee--------------------------------------
   def switch_ee(self, switchValue):
      if (switchValue == False):
         try:
            s.write("ee off\r".encode("utf-8"))
         except:
            print('ee deactive error')    
      else:
         #print(("ee " + str(self.ee[0]) + " " + str(self.ee[1]) + " " + str(self.ee[2]) + " " + str(self.ee[3]) + " " +str(self.ee[4]) + " " +str(self.ee[5]) +"\r").encode("utf-8"))
         try:
            #s.write(("ee on\r").encode("utf-8"))
            s.write(("ee " + str(self.ee[0]) + " " + str(self.ee[1]) + " " + str(self.ee[2]) + " " + str(self.ee[3]) + " " +str(self.ee[4]) + " " +str(self.ee[5]) +"\r").encode("utf-8"))
           
         except:
            print('ee active error')
   def switch_edge(self, switchValue):
      if (switchValue == False):
         try:
            s.write("ee on\r".encode("utf-8"))
         except:
            print('edge deactive error')    
      else:
         try:
            s.write("ee edge\r".encode("utf-8"))
         except:
            print('edge active error')
            
   def slide_ee_gp(self, *args):
      self.ee[0] = int(args[1])
      try:
         s.write(("ee " + "gp " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('ee gp error')         

   def slide_ee_gn(self, *args):
      self.ee[1] = int(args[1])
      try:
         s.write(("ee " + "gn " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('ee gn error')
   def slide_ee_lp(self, *args):
      self.ee[2] = int(args[1])
      try:
         s.write(("ee " + "lp " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('ee lp error')
   def slide_ee_ln(self, *args):
      self.ee[3] = int(args[1])
      try:
         s.write(("ee " + "ln " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('ee ln error')
   def slide_ee_gain(self, *args):
      self.ee[4] = int(args[1])
      try:
         s.write(("ee " + "gain " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('ee coring gain error')
   def slide_ee_flt(self, *args):
      self.ee[5] = 7 - int(args[1])
      try:
         s.write(("ee " + "flt " + str(7-args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('ee flt error')          
#----------------------------3d nr--------------------------------------
   def switch_3dnr(self, switchValue):
      #if (self.ids.switch_3dnr.active == False):
      if (switchValue == False):
         try:
            s.write("3dnr 0 0\r".encode("utf-8"))
         except:
            print('3dnr noise deactive error')   
            #print('3dnr deactive')
      else:
         try:
            #print("3dnr " + str(self.ids.s_3dnr_noise.value) + " " +  str(self.ids.s_3dnr_int.value))
            s.write(("3dnr " + str(self.ids.s_3dnr_int.value) + " " + str(self.ids.s_3dnr_noise.value) +"\r").encode("utf-8"))
         except:
            print('3dnr noise active error')   
   def slide_3dnr_int(self, *args):
      try:
         s.write(("3dnr " + str(args[1]) + " " + str(self.ids.s_3dnr_noise.value) +"\r").encode("utf-8"))
         s.flush()
      except:
         print('3dnr int error')

   def slide_3dnr_noise(self, *args):
      try:
         s.write(("3dnr " + str(self.ids.s_3dnr_int.value) + " " + str(args[1]) + "\r").encode("utf-8"))
         s.flush()
      except:
         print('3dnr noise level error')
#----------------------------gamma--------------------------------------
   def switch_gamma(self, switchValue):
      if (switchValue == False):
         try:
            s.write("gam off\r".encode("utf-8"))
         except:
            print('gamma deactive error')   
            
      else:
         try:
            s.write("gam on\r".encode("utf-8"))
         except:
            print('gamma active error')
            
   def slider_contrast(self, *args):
      try:
         MyLayout.gamvalue[0] = int(args[1]) + 2
         s.write(("gam " + str(MyLayout.gamvalue[0]) + " " + str(MyLayout.gamvalue[1]) + " " + str(MyLayout.gamvalue[2]) + "\r").encode("utf-8"))
         #print(MyLayout.gamvalue)
      except:
         print('Gamma Contrast error')
         
   def slider_d_range(self, *args):
      try:
         MyLayout.gamvalue[1] = int(args[1])
         s.write(("gam " + str(MyLayout.gamvalue[0]) + " " + str(MyLayout.gamvalue[1]) + " " + str(MyLayout.gamvalue[2]) + "\r").encode("utf-8"))
         #print(MyLayout.gamvalue)  
      except:
         print('D-range error')
         
   def slider_knee(self, *args):   
      try:
         MyLayout.gamvalue[2] = int(args[1])
         s.write(("gam " + str(MyLayout.gamvalue[0]) + " " + str(MyLayout.gamvalue[1]) + " " + str(MyLayout.gamvalue[2]) + "\r").encode("utf-8"))
         #print(MyLayout.gamvalue)  
      except:
         print('Knee error')         
#----------------------------end def--------------------------------------         
class MyApp(App):
   def build(self):
      #Window.size = (800, 480)
      self.title = '4K Control'
      return MyLayout()
     
      
if __name__ == '__main__':
   if sys.platform.startswith('win'):
      #print("this is windows")
      ports = ['COM%s' % (i + 1) for i in range(10)]
      
      for port in ports:
         try:
            s = serial.Serial(port, baudrate=115200,bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0.5)
            s.write("ui\r".encode("utf-8"))
            s.flush()
            data = str(s.read(10),'utf-8')
            if 'UIC!' in data:
               s.flush()
               print('>>>>>>>>>>>>',port, '<<<<<<<<<<<< connected!')
               break
            else:
               s.close()
         except:
            pass
            print('no port!')
   else:
      pass
      #print("os not support!")

   
      
   
   if hasattr(sys, '_MEIPASS'):
      resource_add_path(os.path.join(sys._MEIPASS))
   MyApp().run()
   s.close()
   print('>>>>>>>>>>>>',port, '<<<<<<<<<<<< disconnected!')
