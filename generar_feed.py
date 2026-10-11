import os
import datetime
from instaloader import Instaloader, Profile
from feedgen.feed import FeedGenerator

# --- CONFIGURACIÓN ---
# Cambia esto por el usuario de Instagram público que quieres seguir
INSTAGRAM_USER = "elconfidencial" 

def generar_rss_instagram():
    L = Instaloader()
    try:
        perfil = Profile.from_username(L.context, INSTAGRAM_USER)
        
        fg = FeedGenerator()
        fg.id(f'https://instagram.com{INSTAGRAM_USER}')
        fg.title(f'Instagram Feed: @{INSTAGRAM_USER}')
        fg.author({'name': perfil.full_name})
        fg.link(href=f'https://instagram.com{INSTAGRAM_USER}', rel='alternate')
        fg.description(f'Últimas publicaciones de @{INSTAGRAM_USER} en RSS')
        fg.language('es')

        posts = perfil.get_posts()
        contador = 0
        
        for post in posts:
            if contador >= 5:
                break
                
            fe_entry = fg.add_entry()
            fe_entry.id(post.shortcode)
            fe_entry.title(post.caption[:50] + "..." if post.caption else "Publicación de Instagram")
            fe_entry.link(href=f'https://instagram.comp/{post.shortcode}/')
            fe_entry.pubDate(post.date_utc.replace(tzinfo=datetime.timezone.utc))
            
            contenido_html = f'<img src="{post.url}"/><br/><p>{post.caption}</p>'
            fe_entry.content(contenido_html, type='html')
            
            contador += 1

        # Guardamos el archivo final siempre con el mismo nombre
        fg.rss_file("instagram_feed.xml")
        print("¡Archivo XML creado con éxito!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generar_rss_instagram()
