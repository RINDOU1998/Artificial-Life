import numpy as np

def add_fin(list):
    list.append(np.random.uniform(0.02, 0.06))
    list.append(np.random.uniform(0.02, 0.06))
    list.append(np.random.uniform(0.1, 0.2))


def generate_xml_with_modifications(size_modifications, mass_modifications, filename):
    xml_lines = []
    xml_lines.append('<mujoco>')
    xml_lines.append('    <option gravity="0 0 0"/>')
    xml_lines.append('    <worldbody>')
    xml_lines.append('        <light diffuse=".5 .5 .5" pos="0 0 5" dir="0 0 -1"/>')
    xml_lines.append('        <geom type="plane" size="10 10 0.1" rgba=".9 0 0 1"/>')
    xml_lines.append('')
    xml_lines.append('        <body name="fish" pos="0 0 1" euler="0 0 0">')
    xml_lines.append('            <joint type="free" axis="0 0 0" pos="0 0 0" />')
    xml_lines.append('            <body name="body" pos="0 0 0" euler="0 0 0">')
    xml_lines.append('                <geom type="sphere" size="{:.1f}" rgba="0 .9 0 1" mass="{:.5f}" />'.format(size_modifications[0], mass_modifications[0]))
    xml_lines.append('            </body>')
    xml_lines.append('')
    xml_lines.append('            <body name="fin1" pos=".2 0 0" euler="0 -90 0">')
    xml_lines.append('                <joint name="joint1" type="hinge" axis="1 0 0" pos="0 0 .25" range="-45 45" />')
    xml_lines.append('                <geom type="box" size="{:.2f} {:.2f} {:.2f}" rgba="0 0.2 0.7 1" mass="{:.5f}" />'.format(*size_modifications[1:4], mass_modifications[1]))
    xml_lines.append('            </body>')
    xml_lines.append('')
    xml_lines.append('            <body name="fin2" pos="-.2 0 0" euler="0 90 0">')
    xml_lines.append('                <joint name="joint2" type="hinge" axis="1 0 0" pos="0 0 .25" range="-45 45" />')
    xml_lines.append('                <geom type="box" size="{:.2f} {:.2f} {:.2f}" rgba="0 0.2 0.7 1" mass="{:.5f}" />'.format(*size_modifications[4:7], mass_modifications[2]))
    xml_lines.append('            </body>')
    xml_lines.append('')
    xml_lines.append('            <body name="tail" pos="0 0.4 0" euler="0 90 90">')
    xml_lines.append('                <joint name="joint3" type="hinge" axis="0 0 1" pos="0 0 0" range="-45 45" />')
    xml_lines.append('                <geom type="box" size="{:.2f} {:.2f} {:.2f}" rgba="0 0.2 0.7 1" mass="{:.5f}" />'.format(*size_modifications[7:], mass_modifications[3]))
    xml_lines.append('            </body>')
    xml_lines.append('        </body>')
    xml_lines.append('    </worldbody>')
    xml_lines.append('')
    xml_lines.append('    <actuator>')
    xml_lines.append('        <motor joint="joint1" name="t1" gear="10" ctrllimited="true" ctrlrange="-5 5" />')
    xml_lines.append('        <motor joint="joint2" name="t2" gear="10" ctrllimited="true" ctrlrange="-5 5" />')
    xml_lines.append('        <motor joint="joint3" name="t3" gear="10" ctrllimited="true" ctrlrange="-5 5" />')
    xml_lines.append('    </actuator>')
    xml_lines.append('</mujoco>')


    with open(filename, 'w') as f:
        f.write('\n'.join(xml_lines))

# Example usage:
size_modifications=[]
mass_modifications=[]
size_modifications.append(np.random.uniform(0.1, 0.2))
#size of fin1
add_fin(size_modifications)
add_fin(size_modifications)
#add tail
size_modifications.append(np.random.uniform(0.1, 0.2))
size_modifications.append(np.random.uniform(0.01, 0.02))
size_modifications.append(np.random.uniform(0.1, 0.2))
mass_modifications.append(np.random.uniform(0.01, 0.04))
mass_modifications.append(np.random.uniform(0.1, 0.6))
mass_modifications.append(np.random.uniform(0.1, 0.6))
mass_modifications.append(np.random.uniform(0.1, 0.6))




#size_modifications = [0.15, 0.05, 0.01, 0.1, 0.05, 0.01, 0.1, 0.2, 0.02, 0.1]  # New sizes for each body part
#mass_modifications = [0.03, 0.5472251009282674, 0.4046919392945555, 0.4046919392945555]  # New masses for each body part
filename = "modified_model.xml"
generate_xml_with_modifications(size_modifications, mass_modifications, filename)
