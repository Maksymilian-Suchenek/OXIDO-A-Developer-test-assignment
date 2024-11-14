# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from openai import OpenAI
import requests
client = OpenAI()

html_article = open("artykul.html", "w", -1, "utf-8")

request = requests.get("https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt")
#Zakodowanie tekstu z pliku
data = request.text.encode(request.encoding)

prompt = ('Wygeneruj dokument HTML na podstawie niżej podanego tekstu.'
          'Użyj poprawnych tagów HTML; z grafikami obok dłuższych paragrafów,'
          'z użyciem znaczników <img> z atrybutem \"src=image_placeholder.jpg\",'
          'oraz \"alt\" z dokładnym promptem, którego można użyć do wygenerowania grafiki z pomocą AI,'
          'który nie jest streszczeniem artykułu,tylko opisem grafiki, która do niego pasuje;'
          'bez CSS ani JavaScript, zwrócony kod będzie do wstawienia pomiędzy znacznikami <body>,'
          'ale nie zwracaj ich, nie umieszczaj znaczników <html> lub <head>, kod ma być gotowy do wstawienia w innym projekcie.'
          'Pomiń formatowanie z użyciem znaków \"```\". Zwrócony kod ma być w surowym stanie, gotowy do użycia.'
          '\nTekst do obróbki:\n{0}').format(
    data.decode('utf-8')
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
output_prompt = completion.choices[0].message.content

if __name__ == '__main__':
    print(output_prompt)
    html_article.write(output_prompt)
