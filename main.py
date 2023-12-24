import streamlit as st
import time


st.set_page_config(
    page_title="Feliz Natal, Elisa!",
    page_icon="🎅",
)

load_msg = 'Aguarde, uma surpresa está por vir...'
bar = st.progress(0, load_msg)

for i in range(1, 101):
    bar.progress(i, load_msg)
    time.sleep(0.25)

bar.empty()

st.title('Entretenimento não é investimento!')
st.write('Fique atenta e siga as dicas')

url_ft = 'https://g1.globo.com/tecnologia/noticia/2023/12/17/o-que-e-o-jogo-do-tigrinho-e-por-que-ele-e-ilegal-no-brasil.ghtml'
st.link_button(":tiger: Fortune Tiger, vulgo Tigrinho", url_ft, use_container_width=True)

url_ps = 'https://super.abril.com.br/mundo-estranho/como-funciona-um-esquema-de-piramide-financeira/'
st.link_button(':arrow_up_small: É só indicar um amigo...', url_ps, use_container_width=True)

url_fs = 'https://seucreditodigital.com.br/golpe-financeiro-4-sinais-prevenir/'
st.link_button(':money_with_wings: Atente-se, é bom demais para ser verdade!', url_fs, use_container_width=True)

url_ms = 'https://blog.picpay.com/golpes-financeiros/'
st.link_button(':memo: Aqui estão os mais comuns no Brasil', url_ms, use_container_width=True)
