import matplotlib.pyplot as plt
import numpy as np

# Dados dos tempos (em segundos)
etapas = ['BioRemPP', 'KEGG', 'HADEG', 'ToxCSM']
tempos_sem_category = [0.0381, 0.0211, 0.0363, 0.0091]
tempos_com_category = [0.0395, 0.0165, 0.0303, 0.0177]

x = np.arange(len(etapas))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 4))
bars1 = ax.bar(x - width/2, tempos_sem_category, width, label='Sem category')
bars2 = ax.bar(x + width/2, tempos_com_category, width, label='Com category')

ax.set_ylabel('Tempo (segundos)')
ax.set_title('Tempo de execução por etapa do merge')
ax.set_xticks(x)
ax.set_xticklabels(etapas)
ax.legend()
ax.bar_label(bars1, fmt='%.4f')
ax.bar_label(bars2, fmt='%.4f')

plt.tight_layout()
plt.show()
