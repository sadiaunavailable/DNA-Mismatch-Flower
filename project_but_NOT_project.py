import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import random
import pygame
from Bio import SeqIO
import seaborn as sns

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


BACKGROUND_COLOR = (216, 182, 255)  
BUBBLE_COLOR = (255, 255, 255, 128) 

def read_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def find_mutations(ref_seq, mut_seq):
    mutations = []
    for i in range(len(ref_seq)):
        if ref_seq[i] != mut_seq[i]:  
            mutations.append((i, ref_seq[i], mut_seq[i]))
    return mutations

def mutation_to_visual(mutations):
    num_petals = len(mutations) + 3  
    return num_petals

def draw_flower_3D(num_petals):
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.abs(np.sin(num_petals * theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros_like(x)

    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z, mode='lines',
        line=dict(color='white', width=6)
    ))
    
    t = np.linspace(0, 10, 100)
    x_dna = np.sin(t)
    y_dna = np.cos(t)
    z_dna = np.linspace(-5, 5, 100)
    fig.add_trace(go.Scatter3d(
        x=x_dna, y=y_dna, z=z_dna, mode='lines',
        line=dict(color='#8a2be2', width=3)
    ))
    
    fig.update_layout(
        title="DNA Mutation Flower",
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False)
        ),
        showlegend=False,
        plot_bgcolor='#d8b6ff',
        paper_bgcolor='#d8b6ff',
        title_font=dict(size=20, color='#4b0082')
    )
    fig.show()



reference_seq = "AGCT"
mutated_seq = "AGTC"
mutations = find_mutations(reference_seq, mutated_seq)
num_petals = mutation_to_visual(mutations)
draw_flower_3D(num_petals)













"""python3 -m pip install --upgrade pip

sudo apt update
sudo apt install python3-pip
pip install numpy plotly pandas pygame biopython seaborn
"""