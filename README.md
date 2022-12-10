# rasa-chatbot

## Przygotowanie:
1. `rasa init`
2. W utworzonym bazowym modelu podmienić pliki `domain.yml` oraz `nlu.yml` i `stories.yml` z folderu `data`
3. `rasa train`
4. Plik `main.py` można wrzucić do głównego katalogu.
5. W pliku `main.py` podmienić token na swój, ewentualnie zostawić obecny i spróbować dodać bota z [linku](https://discord.com/api/oauth2/authorize?client_id=1047570329880506420&permissions=68608&scope=bot) do własnego serwera.

## Uruchamianie:
1. `rasa run --enable-api`
2. `python main.py`

### Dodatkowe informacje:
- Zadanie jest zrobione na ocenę 3.0. Mimo to można go zapytać o godziny otwarcia i menu (nie jest ono czytane z zewnętrznego pliku).
- Na discordzie można porozmawiać z botem w bezpośrednich wiadomościach lub na kanale tekstowym na serwerze. Aby bot zareagował trzeba przed każdym zdaniem wysłanym do niego dopisać `$bot` na początku.
Przykład:

![image](https://user-images.githubusercontent.com/92596468/206879983-efc21ad5-e135-4c18-a7ff-18bc8fc30c59.png)

