from dm_control import mujoco
import PIL.Image

static_model = """
<mujoco>
<worldbody>
<light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
<geom type="plane" size="1 1 0.1" rgba=".9 0 0 1"/>
<body pos="0 0 1">
<joint type="free"/>
<geom type="box" size=".1 .2 .3" rgba="0 .9 0 1"/>
</body>
</worldbody>
</mujoco>
"""
physics = mujoco.Physics.from_xml_string(static_model)
pixels = physics.render()
image = PIL.Image.fromarray(pixels)
image.show()
image.save(r"C:\Users\Rindou\Artifical Life\image.png")
