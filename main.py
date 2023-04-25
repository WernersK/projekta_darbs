from website import create_app
#Izveidoju strādājošu flask aplikāciju, izmantoju debug automātiskumam.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)