import genesis as gs


gs.init(backend=gs.cpu)

scene = gs.Scene(show_viewer=False,
                 show_FPS=False,
                 vis_options = gs.options.VisOptions(
                    show_world_frame = False
                    ),
)

plane = scene.add_entity(gs.morphs.Plane())
robot = scene.add_entity(
    gs.morphs.URDF(file='ergo/newP.urdf',
                   pos=(0.0, 0.0, 0.4),)
)

follower_camera = scene.add_camera(res=(720, 540),
                                    pos=(0, 0.2, .7),
                                    lookat=(0.0, 0.0, 0.7),
                                    fov=40,
                                    GUI=True)
follower_camera.follow_entity(robot, fixed_axis=(None, None, None), smoothing=0.5, fix_orientation=True)
scene.build()
follower_camera.start_recording()

for i in range(250):
    follower_camera.render()
    scene.step()
    
follower_camera.stop_recording(save_to_filename='video.mp4', fps=60)