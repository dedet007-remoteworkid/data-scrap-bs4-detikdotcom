import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # return 'Tesssttt'
    return render_template('index.html')


@app.route('/detik-pop')
def detik_pop():
    url = 'https://www.detik.com/terpopuler'
    rs = requests.get(url, params={'tag_from': 'framebar'})

    sp = BeautifulSoup(rs.text, 'html.parser')

    pop_area = sp.find(attrs={'class': 'grid-row list-content'})

    judul = pop_area.findAll(attrs={'class': 'media__title'})
    foto = pop_area.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', gambar = foto)


if __name__ == '__main__':
    app.run(debug=True)
