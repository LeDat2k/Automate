import webbrowser
import pyautogui, time
import threading

PATH = r'D:\a.IT\Python\Automate\BrowserDrivers\chromedriver.exe'
EDGE_PATH = r'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(EDGE_PATH))

def init_note(note_link):
    webbrowser.open(note_link)
    time.sleep(1)
    pyautogui.hotkey('win', 'left')
    pyautogui.press('esc')
    return

def init_vocab(vocab_link):
    webbrowser.get('edge').open(vocab_link)
    # time.sleep(2)
    # pyautogui.press('PgDn', presses=3)
    return

def init_dict(dict_link):
	webbrowser.get('edge').open(dict_link)
	return
	
    
try:
    # vocab_link = 'https://www.essentialenglish.review/4000-essential-english-words-2/'
    vocab_link = 'https://www.essentialenglish.review/4000-essential-english-words-3/'
    # vocab_link = 'https://www.essentialenglish.review/4000-essential-english-words-4/'
    # vocab_link = 'https://www.essentialenglish.review/4000-essential-english-words-5/'
    # vocab_link = 'https://www.essentialenglish.review/4000-essential-english-words-6/'
    note_link = 'https://app.simplenote.com/'
    dict_link = 'https://dictionary.cambridge.org/'

    init_note(note_link)
    init_dict(dict_link)
    init_vocab(vocab_link)

except KeyboardInterrupt:
    print('Interrupt')
