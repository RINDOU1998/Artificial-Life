import numpy as np

def create_branch(name, side, z_pos):
    euler_angle = '0 45 0' if side == 'left' else '0 -45 0'
    x_pos = 0.3 if side == 'left' else -0.3
    return [
        f'        <body name="{name}" pos="{x_pos} 0 {z_pos}" euler="{euler_angle}">',
        '            <geom type="cylinder" size=".05 0.5" rgba=".38 .17 .05 1"/>'
    ]

def create_leaf(name, indent_level):
    x_pos = np.random.choice([-0.1, 0.1])
    z_pos = np.random.uniform(-0.3, 0.3)
    indent = ' ' * 4 * indent_level
    return [
        f'{indent}<body name="{name}" pos="{x_pos} 0 {z_pos}">',
        f'{indent}    <joint name="{name}_joint" type="hinge" axis="0 1 0" pos="0 0 0" range="-5 5"/>',
        f'{indent}    <geom type="ellipsoid" size=".04 .02 .01" rgba="0 .5 0 1"/>',
        f'{indent}</body>'
    ]

def create_tree_xml():
    xml_lines = [
        '<mujoco>',
        '    <worldbody>',
        '        <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>',
        '        <geom type="plane" size="5 5 0.1" rgba=".9 0.9 0.9 1"/>',
        '        <body name="trunk" pos="0 0 1.8">',
        '            <joint type="free"/>',
        '            <geom type="cylinder" size=".1 1.8" rgba=".15 .07 .02 1" mass="1000"/>'
    ]

    # np.random initial z positions for the lowest left and right branches
    z_left = np.random.uniform(-1.3, -1)
    z_right = np.random.uniform(-1.1, -0.8)

    leaf_count = 1
    for i in range(1, 4):
        left_branch = create_branch(f'leftbranch{i}', 'left', z_left)
        right_branch = create_branch(f'rightbranch{i}', 'right', z_right)

        for j in range(1, 4):
            left_branch.extend(create_leaf(f'leaf{leaf_count}', 3))
            leaf_count += 1
            right_branch.extend(create_leaf(f'leaf{leaf_count}', 3))
            leaf_count += 1

        left_branch.append('        </body>')
        right_branch.append('        </body>')
        xml_lines.extend(left_branch)
        xml_lines.extend(right_branch)

        z_left = z_right + np.random.uniform(0.4, 0.6)
        z_right = z_left + np.random.uniform(0.4, 0.6)

    xml_lines.extend([
        '        </body>',
        '    </worldbody>',
        '    <actuator>'
    ])

    for i in range(1, leaf_count):
        xml_lines.append(f'        <motor name="leaf{i}_motor" joint="leaf{i}_joint" gear="0.02"/>')

    xml_lines.extend([
        '    </actuator>',
        '</mujoco>'
    ])

    return xml_lines

# Generate XML
tree_xml_lines = create_tree_xml()

# Save to a file using numpy.savetxt
np.savetxt('hw4.xml', tree_xml_lines, fmt='%s')

print("XML saved to hw4.xml")