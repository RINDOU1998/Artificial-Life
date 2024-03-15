from random_g import generate_xml_with_modifications
from random_g import add_fin
from run import run_model
import numpy as np
import csv
import random

#generate parameters
def geno_random_generated(size_modifications,mass_modifications):
    #size of fin1
    size_modifications.append(np.random.uniform(0.1, 0.2))
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

def mutation_random_choose(parent1,parent2):
    size_geno=[]
    mass_geno=[]
    for  size1,size2 in zip(parent1[0],parent2[0]):
        size_geno.append(random.choice([size1, size2]))
    for  mass1,mass2 in zip(parent1[1],parent2[1]):
        mass_geno.append(random.choice([mass1, mass2]))
    child_geno=[size_geno,mass_geno,-1]
    return child_geno

###############
num_generation=5
population_list=[]
size_modifications=[]
mass_modifications=[]
leg_num=3
gear=10
max_fitness=0
generation_fitness_list=[]
max_height_reach=[]
max_distance_travel=[]
###############
geno_random_generated(size_modifications,mass_modifications)


model_filename = "random_model.xml"
generate_xml_with_modifications(size_modifications, mass_modifications, model_filename)

total_distance,max_height,min_height=run_model(model_filename)
print("Total Distance:", total_distance)
print("range", max_height-min_height)
#calculate the fitness
height_fitness=(max_height-min_height)*leg_num*gear
distance_fitness=total_distance*leg_num*gear
total_fitness=height_fitness+distance_fitness

#generate population

start_fitness=0
start_height=0
start_distance=0

for i in range(10):
    size_modifications=[]
    mass_modifications=[]
    geno_random_generated(size_modifications,mass_modifications)
    model_filename = "random_model.xml"
    generate_xml_with_modifications(size_modifications, mass_modifications, model_filename)
    total_distance,max_height,min_height=run_model(model_filename)
    print("Total Distance:", total_distance)
    print("range", max_height-min_height)
    #calculate the fitness
    height_fitness=(max_height-min_height)*leg_num*gear
    distance_fitness=total_distance*leg_num*gear
    total_fitness=height_fitness+distance_fitness
    start_fitness+=total_fitness
    h_r=max_height-min_height
    print("Fitness: ", total_fitness)
    if total_fitness>max_fitness:
        max_fitness=total_distance
    population_list.append([size_modifications,mass_modifications,total_fitness])
    if total_distance>start_distance:
        start_distance=total_distance
    if h_r>start_height:
        start_height=h_r

max_height_reach.append(start_height)
max_distance_travel.append(start_distance)
generation_fitness_list.append(start_fitness)

population_list = sorted(population_list, key=lambda x: x[2])
print('population of generation 0: ',population_list)
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in population_list:
        writer.writerow(row)

#take half and mix their genotype

mate_list=population_list[5:]

child_list=[]

for i in range(len(mate_list)):
    for j in range(i + 1, len(mate_list)):
       child_geno=mutation_random_choose(mate_list[i],mate_list[j])
       child_list.append(child_geno)

print("child_generated",child_list)


# for each generation, mutation and choose child for mate
for i in range(num_generation):
    generation_fitness=0
    #run each child geno
    max_height=0
    max_distance=0
    
    for ele in child_list:
        size_modifications=ele[0]
        mass_modifications=ele[1]
        model_filename = "child_model.xml"
        generate_xml_with_modifications(size_modifications, mass_modifications, model_filename)
        total_distance,max_height,min_height=run_model(model_filename)
        print("Total Distance:", total_distance)
        print("range", max_height-min_height)
        #calculate the fitness
        height_fitness=(max_height-min_height)*leg_num*gear
        distance_fitness=total_distance*leg_num*gear
        total_fitness=height_fitness+distance_fitness
        generation_fitness+=total_fitness
        print("Fitness: ", total_fitness)
        ele[2]=total_fitness
        if total_distance>max_height:
            max_height=total_distance
        if (max_height-min_height)>max_distance:
            max_distance=(max_height-min_height)

    max_height_reach.append(max_height)
    max_distance_travel.append(max_distance)

    #record the generation
    generation_fitness_list.append(generation_fitness)
    population_list = sorted(child_list, key=lambda x: x[2])
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in population_list:
            writer.writerow(row)
    mate_list=population_list[5:]
    child_list=[]
    for i in range(len(mate_list)):
        for j in range(i + 1, len(mate_list)):
            child_geno=mutation_random_choose(mate_list[i],mate_list[j])
            child_list.append(child_geno)
    print("child_generated",child_list)

print("generation_fitness: ",generation_fitness_list)
print("max height reach",max_height_reach )
print("max distance travel",max_distance_travel )