prompt : 1. Faites une recherche pour en trouver 2 ou 3, les plus variés possibles. Vous pouvez essayer de trouver des benchmarks qui testent des sujets qui vous intéressent (science, programmation, mathématiques, écriture de fiction, etc.). 2. Créer un petit tableau avec des informations générales sur les benchmarks. 3. Quelles compétences des IA mesurent vos benchmarks ? 4. Trouver quelques questions et regardez les réponses des modèles locaux, ainsi que ceux des grands modèles. Quelles sont vos impressions ? 5. Cherchez les résultats des modèles sur vos benchmarks sur des sites de références. Comment ont évolué les scores des meilleurs modèles depuis la publication du benchmark.

Voici une réponse structurée qui pourrait servir directement pour un rapport ou devoir. J’ai choisi 3 benchmarks assez différents : connaissances générales, programmation et mathématiques.
1. Recherche de 3 benchmarks variés
Je prends :
MMLU (Massive Multitask Language Understanding) → connaissances générales
HumanEval (OpenAI Code Generation Benchmark) → programmation
GSM8K (Grade School Math 8K) → raisonnement mathématique
Ces benchmarks sont parmi les plus utilisés pour évaluer les grands modèles de langage (LLM).
2. Tableau comparatif des benchmarks
Benchmark	Domaine	Type de tâches	Taille	Métrique
MMLU	Connaissances générales	QCM dans de nombreux domaines (histoire, médecine, droit…)	~15 000 questions	Accuracy
HumanEval	Programmation	Génération de fonctions Python à partir d’une description	164 problèmes	pass@k (tests unitaires)
GSM8K	Mathématiques	Problèmes de maths niveau primaire nécessitant plusieurs étapes	~8 500 problèmes	Exact match de la réponse
pass@k : probabilité qu’au moins une solution générée passe les tests.
Ces benchmarks permettent de comparer objectivement différents modèles.
3. Compétences mesurées par ces benchmarks
1️⃣ MMLU
Mesure surtout :
connaissances encyclopédiques
compréhension de texte
raisonnement académique
capacité à répondre à des questions dans 57 disciplines
➡️ Permet d’évaluer le niveau général de culture et de raisonnement d’un modèle.
2️⃣ HumanEval
Mesure :
génération de code
compréhension d’algorithmes
logique de programmation
capacité à produire un code qui passe des tests
➡️ Mesure la fiabilité en programmation.
3️⃣ GSM8K
Mesure :
raisonnement mathématique
résolution de problèmes en plusieurs étapes
capacité à décomposer un problème
➡️ Benchmark classique pour tester le raisonnement logique des LLM.
4. Exemple de questions et comparaison des réponses
Exemple GSM8K
Question :
Natalie a vendu 48 clips en avril et la moitié en mai.
Combien en a-t-elle vendus au total ?
Réponse correcte
48 + 24 = 72
Modèles locaux (petits modèles open-source)
Souvent :
oublient une étape
donnent directement 48 + 48
ou une mauvaise interprétation
Exemple typique :
Elle a vendu 48 en avril et 48 en mai → 96
❌ erreur de raisonnement.
Grands modèles
Les grands modèles font souvent :
48 / 2 = 24
48 + 24 = 72
✔ réponse correcte.
Cela montre que les grands modèles gèrent mieux le raisonnement multi-étapes.
Exemple HumanEval
Question :
Write a function that returns the factorial of a number.
Mauvaise réponse typique (petits modèles)
oublie les cas limites
erreur de récursion
code qui ne compile pas
Bonne réponse (grands modèles)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
✔ passe les tests.
Impression générale
Les différences principales :
Type de modèle	Comportement
petits modèles locaux	erreurs logiques fréquentes
grands modèles	raisonnement plus structuré
modèles récents	expliquent les étapes
Les performances dépendent beaucoup :
du nombre de paramètres
du training
de techniques comme Chain-of-Thought.
5. Évolution des scores sur les benchmarks
GSM8K (maths)
Progression spectaculaire :
Année	Modèle	Score
2020	GPT-3	~4.9 %
2022	GPT-3.5	57 %
2023	GPT-4	92 %
2024	Claude 3.5	96 %
➡️ Les modèles sont passés de quasi aléatoire à presque parfait.
HumanEval (programmation)
Exemples de scores récents :
Modèle	HumanEval pass@1
GPT-4	~67 %
GPT-4 Turbo	~87 %
Claude 3 Opus	~85 %
Llama 3 70B	~82 %
Les performances ont beaucoup progressé avec les modèles récents.
MMLU
Exemples :
Modèle	Score MMLU
GPT-3.5	~70 %
GPT-4	~86 %
GPT-4o	~88 %
➡️ Les modèles atteignent presque le niveau expert humain sur certaines disciplines.
Conclusion
Les benchmarks comme MMLU, HumanEval et GSM8K permettent d’évaluer différentes compétences des IA :
📚 connaissances générales
💻 programmation
🧠 raisonnement mathématique
On observe une amélioration extrêmement rapide des performances des modèles depuis 2020, avec certains benchmarks presque saturés aujourd’hui.
Cependant, ces benchmarks ont aussi des limites :
possible sur-apprentissage (benchmark contamination)
questions parfois trop académiques
scores élevés ≠ toujours performance réelle.
✅ Si tu veux, je peux aussi te montrer comment tester toi-même un modèle local (Ollama, Llama, etc.) sur ces benchmarks, ce qui peut être très intéressant pour ton devoir.
