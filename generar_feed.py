import os
import datetime
from feedgen.feed import FeedGenerator

# --- CONFIGURACIÓN ---
INSTAGRAM_USER = "elconfidencial" 

def generar_rss_instagram():
    try:
        fg = FeedGenerator()
        fg.id(f'https://instagram.com/{INSTAGRAM_USER}')
        fg.title(f'Instagram Feed: @{INSTAGRAM_USER}')
        fg.link(href=f'https://instagram.com/{INSTAGRAM_USER}', rel='alternate')
        fg.description(f'Últimas publicaciones de @{INSTAGRAM_USER} en RSS')
        fg.language('es')

        fe_entry = fg.add_entry()
        fe_entry.id(f"post_{INSTAGRAM_USER}_{datetime.date.today().strftime('%Y%m%d')}")
        fe_entry.title(f"Ver nuevas publicaciones de @{INSTAGRAM_USER}")
        
        url_libre = f'https://picuki.com{INSTAGRAM_USER}'
        fe_entry.link(href=url_libre)
        fe_entry.pubDate(datetime.datetime.now(datetime.timezone.utc))
        
        contenido_html = f'''
        <p>Las restricciones de Instagram bloquean el acceso directo, pero puedes ver todo el contenido actualizado haciendo clic aquí:</p>
        <p><a href="{url_libre}"><b>→ Ver fotos y posts recientes de @{INSTAGRAM_USER} sin bloqueos ←</b></a></p>
        '''
        fe_entry.content(contenido_html, type='html')

        fg.rss_file("instagram_feed.xml")
        print("¡Archivo XML creado con éxito!")
        
    except Exception as e:
        print(f"Error al generar el feed: {e}")

if __name__ == "__main__":
    generar_rss_instagram()
