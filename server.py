from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, Markup
app = Flask(__name__)

data = {
      1: {
        'id': 1,
        'name': 'Banda', 
        'description': 'Banda, originating from the state of Sinaloa, is an ensemble typically consisting of 8 to 24 members, playing a mix of brass, and wind instruments like trumpets, trombones, clarinets, and a variety of percussion instruments. Characterized by the prominent use of drums and the absence of string instruments and accordions, banda ensembles usually include one to three vocalists.',
        'audio1': '../static/Audios/Banda/El Mechón - Banda MS.mp3',
        'image': '../static/Audios/Banda/Banda.png',
        'count': 0
      },
      2: {
         'id': 2,
         'name': 'Mariachi', 
         'description': 'Mariachi is popular in western Mexico and is typically performed through an ensemble of musicians with a main singer, violins, vihuelas, guitars, guitarróns, and trumpets. Mariachi is usually characterized by the main singer’s slight shaking in vocal notes, and el grito, a cathartic, joyous yell.',
         'audio1': '../static/Audios/Mariachi/Volver, Volver - Vicente Fernandez.mp3',
         'image': "../static/Audios/Mariachi/Mariachi.png",
         'count': 0
      },
      3: {
         'id': 3,
         'name': 'Norteño', 
         'description': 'Norteño emerged within the Northern states of Mexico as is reminiscent of the folk music of German, Polish, and Czech immigrants brought to Mexico. The accordion and bajo sexto are Norteño’s most characteristic instruments, but trumpets, alto and tenor saxophones, guitar, bass, and drums are also heavily used.',
         'audio1': '../static/Audios/Norteño/La Puerta Negra - Los Tigres Del Norte.mp3',
         'image': "../static/Audios/Norteño/Norteño.png",
         'count': 0
      },
      4: {
         'id': 4,
         'name': 'Son Mexicano', 
         'description': 'Son Mexicano is a traditional Mexican folk music style prevalent in states along the Gulf of Mexico, characterized by its reliance on a variety of string instruments like guitars, violins, and harps. Accompanied by social dances that often feature rhythmic stomping on raised platforms to augment percussion, the genre also incorporates instruments such as the vihuela, guitarrón, and various percussive elements like tambors and cajóns.',
         'audio1': '../static/Audios/Son Mexicano/La Bruja - Tlen Huicani.mp3',
         'image': "../static/Audios/Son Mexicano/SonMexicano.png",
         'count': 0
      },
      5: {
         'id': 5,
         'name': 'Cumbia Sonidera', 
         'description': 'Cumbia Sonidera is particularly popular in Mexico City and the state of Puebla. This genre is characterized by its unique incorporation of electronic elements such as voice and pitch alterations, alongside traditional sounds from the guacharaca (a percussive instrument) and organ.',
         'audio1': '../static/Audios/Cumbia Sonidera/Como Te Voy A Olvidar - Los Angeles Azules.mp3',
         'image': "../static/Audios/Cumbia Sonidera/CumbiaSonidera.png",
         'count': 0
      },
      6: {
         'id': 6,
         'name': 'Chilena', 
         'description': 'Chilena, a music genre named after its Chilean influences, originated from the fusion of music introduced by Chilean sailors and the mestizo traditions of southern Mexico, particularly in Oaxaca and Guerrero. This representative genre is embraced by indigenous, Afro-Mexican, and mestizo communities, featuring instruments such as the guitar, bajo quinto, violin, and harp.',
         'audio1': '../static/Audios/Chilena/CHILENA MIXTECA - GRUPO SOBERANO DE TIERRA MIXTECA.mp3',
         'image': "../static/Audios/Chilena/Chilena.png",
         'count': 0
      }
}

dataQuestions = {
   1:{
      'id': 1,
      'question': 'What region does the following musical piece belong to?',
      'audio': '../static/Audios/Cumbia Sonidera/Tus Jefes No Me Quieren - Grupo Ensamble.mp3',
      'answer': 'Cumbia Sonidera',
      'choice1': 'Banda',
      'choice2': 'Mariachi',
      'choice3': 'Norteño',
      'choice4': 'Son Mexicano',
      'choice5': 'Cumbia Sonidera',
      'choice6': 'Chilena',
   },
   2:{
      'id': 2,
      'question': 'What region does the following musical piece belong to?',
      'audio': '../static/Audios/Norteño/Los Chismes - Chalino Sanchez.mp3',
      'answer': 'Norteño',
      'choice1': 'Banda',
      'choice2': 'Mariachi',
      'choice3': 'Norteño',
      'choice4': 'Son Mexicano',
      'choice5': 'Cumbia Sonidera',
      'choice6': 'Chilena',
   },
   3:{
      'id': 3,
      'question': 'What region does the following musical piece belong to?',
      'audio': '../static/Audios/Chilena/Mixteca Hermosa - Grupo Santa Cruz.mp3',
      'answer': 'Chilena',
      'choice1': 'Banda',
      'choice2': 'Mariachi',
      'choice3': 'Norteño',
      'choice4': 'Son Mexicano',
      'choice5': 'Cumbia Sonidera',
      'choice6': 'Chilena',
   },
   4:{
      'id': 4,
      'question': 'What region does the following musical piece belong to?',
      'audio': '../static/Audios/Mariachi/Te Vas a Quedar Con las Ganas - Aida Cuevas.mp3',
      'answer': 'Mariachi',
      'choice1': 'Banda',
      'choice2': 'Mariachi',
      'choice3': 'Norteño',
      'choice4': 'Son Mexicano',
      'choice5': 'Cumbia Sonidera',
      'choice6': 'Chilena',
   },
   5:{
      'id': 5,
      'question': 'What region does the following musical piece belong to?',
      'audio': '../static/Audios/Son Mexicano/El Tilingo Lingo - Conjunto Jarocho.mp3',
      'answer': 'Son Mexicano',
      'choice1': 'Banda',
      'choice2': 'Mariachi',
      'choice3': 'Norteño',
      'choice4': 'Son Mexicano',
      'choice5': 'Cumbia Sonidera',
      'choice6': 'Chilena',
   },
   6:{
      'id': 6,
      'question': 'What region does the following musical piece belong to?',
      'audio': '../static/Audios/Banda/La Niña Fresa - Banda Zeta.mp3',
      'answer': 'Banda',
      'choice1': 'Banda',
      'choice2': 'Mariachi',
      'choice3': 'Norteño',
      'choice4': 'Son Mexicano',
      'choice5': 'Cumbia Sonidera',
      'choice6': 'Chilena',
   }
}

# ROUTES
@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/map')
def map():
   return render_template('map.html')


@app.route('/quiz/<int:item_id>')
def quiz(item_id):
   item = dataQuestions.get(item_id)
   if item:
      return render_template('quiz.html', item=item)
   else:
      return "Item not found", 404

@app.route('/learn/<int:item_id>')
def view_item(item_id):
    item = data.get(item_id)
    if item:
        return render_template('learn.html', item=item)
    else:
        return "Item not found", 404
   
@app.route('/congrats')
def congrats():
   return render_template("congrats.html")

if __name__ == '__main__':
   app.run(debug = True)