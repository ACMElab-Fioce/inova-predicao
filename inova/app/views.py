import matplotlib.pyplot as plt
import pandas as pd
from django.views import View
from django.shortcuts import render
from app.models import ClassiFinDtNotific
import io
import urllib, base64

class HomePage(View):
    def get(self, request):
        dados = ClassiFinDtNotific.objects.values('classi_fin', 'quantidade', 'dt_notific')
        df = pd.DataFrame.from_records(dados)

        #Apenas Dengue
        dfdengue = df[df['classi_fin'].isin(['Dengue', 'Dengue grave', 'Dengue com sinais de alarme'])]
        df_grouped_dengue = dfdengue.groupby('dt_notific')['quantidade'].sum().reset_index()
        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#121212')
        ax.set_facecolor('#121212')
        ax.bar(df_grouped_dengue['dt_notific'], df_grouped_dengue['quantidade'], color='#9b59b6')
        ax.set_xlabel('Período', color='white', fontsize=14)
        ax.set_ylabel('Quantidade total', color='white', fontsize=14)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        plt.xticks(rotation=45, ha='right')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format='png', transparent=True)
        buf.seek(0)
        string = base64.b64encode(buf.read())
        graph_data_dengue = urllib.parse.quote(string)
        plt.close(fig)  

        #Apenas Dengue com sinais de alarme
        dfdenguegrave = df[df['classi_fin'] == 'Dengue com sinais de alarme']
        df_grouped_denguegrave = dfdenguegrave.groupby('dt_notific')['quantidade'].sum().reset_index()
        plt.style.use('dark_background')
        fig2, ax = plt.subplots()
        fig2.patch.set_facecolor('#121212')
        ax.set_facecolor('#121212')
        ax.bar(df_grouped_denguegrave['dt_notific'], df_grouped_denguegrave['quantidade'], color='#fa7e1e')
        ax.set_xlabel('Período', color='white', fontsize=14)
        ax.set_ylabel('Quantidade total', color='white', fontsize=14)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        plt.xticks(rotation=45, ha='right')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        plt.tight_layout()
        buf2 = io.BytesIO()
        plt.savefig(buf2, format='png', transparent=True)
        buf2.seek(0)
        string = base64.b64encode(buf2.read())
        graph_data_denguealarme = urllib.parse.quote(string)
        plt.close(fig2)

        #Apenas Dengue grave
        dfdenguegrave = df[df['classi_fin'] == 'Dengue grave']
        df_grouped_denguegrave = dfdenguegrave.groupby('dt_notific')['quantidade'].sum().reset_index()
        plt.style.use('dark_background')
        fig3, ax = plt.subplots()
        fig3.patch.set_facecolor('#121212')
        ax.set_facecolor('#121212')
        ax.bar(df_grouped_denguegrave['dt_notific'], df_grouped_denguegrave['quantidade'], color='#d62976')
        ax.set_xlabel('Período', color='white', fontsize=14)
        ax.set_ylabel('Quantidade total', color='white', fontsize=14)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        plt.xticks(rotation=45, ha='right')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        plt.tight_layout()
        buf3 = io.BytesIO()
        plt.savefig(buf3, format='png', transparent=True)
        buf3.seek(0)
        string = base64.b64encode(buf3.read())
        graph_data_denguegrave = urllib.parse.quote(string)
        plt.close(fig3)

        # Renderizar o template com os dois gráficos em base64
        return render(request, 'index.html', {'graph_data_dengue': graph_data_dengue, 'graph_data_denguegrave': graph_data_denguegrave, 'graph_data_denguealarme': graph_data_denguealarme})
