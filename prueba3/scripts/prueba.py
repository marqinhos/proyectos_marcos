#!/usr/bin/env python     
# license removed for brevity    
 
import rospy
from std_msgs.msg import String 
#importante el primer comentario no dejar un espacio
def talker():    
    pub2 = rospy.Publisher('num', String, queue_size=10)  # que diferencia hay en el nombre ''   
    rospy.init_node('talker', anonymous=True) # porque pone talker

    counter = str(input('Escribe un valor cabezon: '))  
    num =  'hola soy el numero: {} {}'.format(counter, '\n')
    rospy.loginfo(num) # porque no se puede quitar esto
    pub2.publish(num)


    """while not rospy.is_shutdown():         
        numero = "%d" % counter         
        counter += 1
        rospy.loginfo(hello_str)         
        pub.publish(hello_str)         
        rate.sleep()"""

if __name__ == '__main__':     
    try:         
        talker()     
        
    except rospy.ROSInterruptException:         
        pass 
