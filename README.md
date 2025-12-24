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

3.1. NavОго в RViz:

1) Откройте RViz
2) В левой панели найдите инструмент "2D Nav Goal"
3) Кликните на карте в точку, куда должен добраться робот
4) Робот автоматически построит маршрут и доедет туда

3.2.Управление манипулятором в MoveIt:

1) В окне MoveIt выберите нужную позу для манипулятора
2) Нажмите "Plan" для планирования траектории
3) Нажмите "Execute" для выполнения движения
