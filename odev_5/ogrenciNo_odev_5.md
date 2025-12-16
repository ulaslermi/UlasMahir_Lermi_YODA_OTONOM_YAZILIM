Ulaş Mahir Lermi
23015042

ROS 2 GENEL KOMUTLARI

ros2 –help = ros2 aktif ve kullanılabilir olup olmadığına bakılır

turtlesim_node (ros2 run turtlesim turtlesim_node)= ros2 nin çalıştığı doğrulanır ve simulasyon ortamı başlatılır.

 ros2 run turtlesim turtle_teleop_key = klavyede yön tuşları ile kaplumbağa hareket eder

ros2 node list
ros2 topic list
ros2 service list     bu kodlarla liste şeklinde bilgileri görebiliyoruz.
ros2 action list

mkdir -p ~/ros2_ws/src = ros2_ws adında bir workspace oluşturulur.

cd ~/ros2_ws = workspace e girer.

colcon build = buildi derlemeyi ve paket yönetimi yapan ana araç.

source install/setup.bash = colcon paketleri install altına koyar source edince ros2 bunları görür.

ros2 pkg create turtle_controller --build-type ament_python --dependencies rclpy geometry_msgs = ros2 için paket oluşturur
(turtle_controller = paketin adı , ament_python = pythonile node yazılcak , rclpy = ros2 python API , geometry_msgs =twist mesajı burda)

ls turtle_controller = paketin içine bakarız (package.xml =paket kimliği , setup.py =python paket ayarları ve python tarafında hangi dosya çalıştırılır onu söyler. , turtle_controller/ = node kodlarını yazacağın klasör.)

cd ~/ros2_ws
colcon build
source install/setup.bash paketi = ros2 ye tanıtır

2 terminal açtım birinde turtle oluşturdum diğerinde 
ros2 run turtle_controller twist_pub kodu ile kendi kendine hareket etmesini sağladım.Twist tipinde hız mesajları ile kontrol edildi.

nano twist_pub.py =twist_pub.py dosyası oluşturup içine dönmesi için kod yazıldı.
