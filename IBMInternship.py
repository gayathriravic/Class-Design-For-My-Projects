"""
We have these classes here.
1. Generator model. --> initial generation + generation after prediction.
2. Prediction Model --> reads the annotations and generates again.
3. Users --> annotates the data and then sends it to the model.


PROCESS:
1. Create a Generator class. this will implement web scraping, initial generation of jokes and also the final user-specific jokes.
2. create a user class. this should inherit the generator class. this will access the jokes generated and the users will annotate them.
3. create a model class. this is our machine learning model that will learn from the user annotations.
4. then send this model to the generator class to further generate jokes of the user preferences.

"""
class Generator():
    def __init__(self):
        self.data = []
        self.jokes = []

    def webScrape(self):   #### topics according to the services provided by customer service chat-bot.
        #dataSet = open('path to ngram dataset')
        dataSet = {'animals':['dog','cat'],'cosmetics':['makeup','lipstick'],'food':['pizza']}
        # form the topics. (uncommented it so that the program runs)
        # calculate co-occurence counts and append them to file.

    def initialGeneration(self):
        #for all the topics!
        #analyze co-occurence counts to form a valid sentence.
        #analyze phonetics through CMU pronunciation dictionary.
        #analyze alliterations.
        #words that have a double meaning
        #analyze twists in the sentence.
        # then generate a set of jokes.
        self.jokes = ['i saw','yes i know','haha']

    def generateNewJokes(self,model):
        print("generating user-specific jokes")
        return self.jokes


class User(Generator):
    def __init__(self,g):
        self.annotations = g.jokes
        self.annotations_list = []

    def annotate(self):
        i = 0
        for jokes in self.annotations:
            if i%2 == 0:
                self.annotations_list.append(1)
            else:
                self.annotations_list.append(0)
            i += 1

class Model():
    def __init__(self):
        self.MLmodel = None

    def learn_features(self,annotations):
        self.MLmodel = "Random forest model"


if __name__ == '__main__':
    g = Generator()
    g.initialGeneration()
    user = User(g)
    user.annotate()
    model = Model()
    model.learn_features(user.annotations_list)
    jokes = g.generateNewJokes(model.MLmodel)
    print("User specific jokes are",jokes)
