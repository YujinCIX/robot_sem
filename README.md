# robot_sem

1. Сборка проекта:
```
cd ~/robotics/ros2_ws
colcon build --symlink-install
source install/setup.bash
```
2. Запуск проекта:

Вариант 1: ПОЛНЫЙ ЗАПУСК (Gazebo + RViz + Nav2 + SLAM)
```
ros2 launch your_robot_description complete_demo.launch.py
```
Функциональность после запуска
1) Gazebo: Симуляция робота в коридоре с препятствиями
2) RViz: Визуализация робота, лидара, построение карты
3) Nav2: Навигация робота (установка целевой точки кликом в RViz)
4) SLAM: Построение карты в реальном времени
5) MoveIt: Управление 6-осевым манипулятором



Вариант 2: Отдельные компоненты (в разных терминалах)
```
# Терминал 1: Gazebo + Robot State Publisher + Controllers
ros2 launch your_robot_description gazebo.launch.py

# Терминал 2: RViz (после загрузки Gazebo)
ros2 launch your_robot_description rviz.launch.py

# Терминал 3: SLAM
ros2 launch your_robot_description slam.launch.py

# Терминал 4: Nav2
ros2 launch your_robot_description nav2.launch.py
```

Вариант 3: MoveIt для управления манипулятором
```
# Терминал 1: Gazebo
ros2 launch your_robot_description gazebo.launch.py

# Терминал 2: MoveIt2 (после загрузки Gazebo)
ros2 launch your_robot_description moveit.launch.py
```

3. Управление роботом:

3.1. Nav2 в RViz:

1) Откройте RViz
2) В левой панели найдите инструмент "2D Nav Goal"
3) Кликните на карте в точку, куда должен добраться робот
4) Робот автоматически построит маршрут и доедет туда

3.2.Управление манипулятором в MoveIt:

1) В окне MoveIt выберите нужную позу для манипулятора
2) Нажмите "Plan" для планирования траектории
3) Нажмите "Execute" для выполнения движения

4. Полная структура проекта:

~/robotics/
  ros2_ws/
    src/
      your_robot_description/
        CMakeLists.txt
        package.xml
        urdf/
          robot.urdf.xacro          (главный файл URDF)
          base.urdf.xacro           (платформа + колеса)
          manipulator.urdf.xacro    (6-звенный манипулятор)
          sensors.urdf.xacro        (лидар + камера)
          gazebo.urdf.xacro         (Gazebo плагины)
        config/
          controller_manager.yaml   (ros2_control параметры)
          moveit_controllers.yaml   (MoveIt контроллеры)
          joint_limits.yaml         (ограничения суставов)
          nav2_params.yaml          (параметры навигации)
          bridge_config.yaml        (Gazebo-ROS мост)
        launch/
          gazebo.launch.py          (запуск Gazebo)
          robot_state_publisher.launch.py (TF трансформации)
          rviz.launch.py            (визуализация RViz)
          slam.launch.py            (SLAM Toolbox)
          nav2.launch.py            (навигация)
          moveit.launch.py          (MoveIt2)
          complete_demo.launch.py   (всё вместе)
        rviz/
          robot_config.rviz         (конфиг для навигации)
          moveit_config.rviz        (конфиг для манипулятора)
        worlds/
          corridor_world.world      (мир с коридором и препятствиями)
    build/
    install/
    log/
