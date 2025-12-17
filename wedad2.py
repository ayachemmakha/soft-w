import streamlit as st
import datetime

# Configuration de la page
st.set_page_config(page_title="Soft Skills App", page_icon="🧠", layout="wide")

st.title("🧠 Soft Skills Assessment App")

# Sidebar
st.sidebar.header("📊 Paramètres")
skill = st.sidebar.selectbox(
    "Choisissez la compétence à évaluer",
    ("Gestion du stress", "Gestion du temps", "Gestion des conflits & Intelligence émotionnelle", 
     "Adaptation au changement", "Intelligence financière", "Résolution de problèmes", "Leadership")
)

# Main content
st.sidebar.markdown("---")
st.sidebar.info("""
### 📝 Instructions
1. Entrez votre nom
2. Répondez à toutes les questions
3. Cliquez sur "Voir le résultat"
""")

# Store date in session state
if 'date' not in st.session_state:
    st.session_state.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Nom de l'utilisateur
name = st.text_input("Entrez votre nom", placeholder="Votre nom ici...")

if name:
    st.success(f"Bienvenue {name} 👋 - Compétence sélectionnée: **{skill}**")
    
    # Initialize variables for all skills
    questions = []
    bonnes = []
    videos = []
    resources = ""
    
    # ---------------- Gestion du stress ----------------
    if skill == "Gestion du stress":
        st.header("😌 Gestion du stress")
        
        # Définition détaillée
        with st.expander("📖 Définition complète et théorie", expanded=True):
            st.markdown("""
            **Définition complète :**
            La gestion du stress est l'ensemble des techniques et stratégies permettant de faire face aux situations stressantes de manière efficace. 
            Elle implique la reconnaissance des facteurs de stress, le développement de mécanismes d'adaptation sains et le maintien d'un équilibre 
            entre vie professionnelle et personnelle.
            
            **Théorie :**
            - **Stress aigu vs chronique :** Le stress aigu est une réponse immédiate à une menace, tandis que le stress chronique est prolongé et peut être nocif pour la santé
            - **Réponse au stress :** Le corps réagit par la libération d'hormones (cortisol, adrénaline)
            - **Facteurs de stress :** Travail, relations, finances, santé
            - **Conséquences :** Burnout, problèmes de santé, diminution des performances
            
            **Compétences clés à développer :**
            1. **Reconnaissance des signes de stress** (physiques, émotionnels, comportementaux)
            2. **Techniques de relaxation** (respiration, méditation)
            3. **Gestion du temps** pour réduire la pression
            4. **Communication assertive** pour exprimer ses besoins
            5. **Resilience émotionnelle** pour rebondir face aux difficultés
            
            **Modèles théoriques :**
            - **Modèle transactionnel de Lazarus et Folkman :** Le stress résulte de l'interaction entre la personne et son environnement
            - **Théorie de l'équilibre de Karasek :** L'équilibre entre exigences du travail et contrôle sur ces exigences
            """)

        st.subheader("📝 Test – Situations réelles")
        
        # Create columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.radio("1. Examen demain, pas prêt :", 
                         ["Organiser le temps", "Paniquer", "Tout abandonner"], 
                         key="s1")
            q3 = st.radio("3. Problème inattendu :", 
                         ["Rester calme", "Se bloquer", "Accuser quelqu'un"], 
                         key="s3")
            q5 = st.radio("5. Stress et sommeil :", 
                         ["Rarement", "Parfois", "Souvent"], 
                         key="s5")
            q7 = st.radio("7. Pression au travail :", 
                         ["Discuter calmement", "S'énerver", "S'isoler"], 
                         key="s7")
            q9 = st.radio("9. Après une erreur :", 
                         ["Corriger et apprendre", "Se culpabiliser", "Blâmer les autres"], 
                         key="s9")
            q11 = st.radio("11. Conflit sous stress :", 
                          ["Dialoguer calmement", "Se fermer", "Crier"], 
                          key="s11")
            q13 = st.radio("13. Face à un imprévu :", 
                          ["S'adapter rapidement", "Se plaindre", "Ignorer le problème"], 
                          key="s13")
            
        with col2:
            q2 = st.radio("2. Tâche urgente :", 
                         ["Organiser et demander clarification", "Stresser", "Éviter"], 
                         key="s2")
            q4 = st.radio("4. Sous stress élevé :", 
                         ["Techniques de respiration", "Arrêter tout", "Exploser de colère"], 
                         key="s4")
            q6 = st.radio("6. Trop de tâches :", 
                         ["Prioriser", "Tout faire d'un coup", "Abandonner"], 
                         key="s6")
            q8 = st.radio("8. Organisation du temps :", 
                         ["Toujours planifier", "Parfois planifier", "Rarement planifier"], 
                         key="s8")
            q10 = st.radio("10. Avant un entretien :", 
                          ["Bien préparer", "Stresser beaucoup", "Improviser"], 
                          key="s10")
            q12 = st.radio("12. Journée difficile :", 
                          ["Demander soutien", "Tout garder", "S'isoler"], 
                          key="s12")
            q14 = st.radio("14. Sous pression prolongée :", 
                          ["Prendre des pauses et respirer", "Travailler sans arrêt", "Quitter"], 
                          key="s14")
        
        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14]

        bonnes = [
            "Organiser le temps",
            "Organiser et demander clarification",
            "Rester calme",
            "Techniques de respiration",
            "Rarement",
            "Prioriser",
            "Discuter calmement",
            "Toujours planifier",
            "Corriger et apprendre",
            "Bien préparer",
            "Dialoguer calmement",
            "Demander soutien",
            "S'adapter rapidement",
            "Prendre des pauses et respirer",
        ]

        videos = [
            "https://www.youtube.com/watch?v=hnpQrMqDoqE",
            "https://www.youtube.com/watch?v=ZToicYcHIOU",
            "https://www.youtube.com/watch?v=odADwWzHR24",
        ]
        resources = "📚 [Guide complet de gestion du stress](https://example.com)"

    # ---------------- Gestion du temps ----------------
    elif skill == "Gestion du temps":
        st.header("⏰ Gestion du temps")
        
        with st.expander("📖 Définition complète et théorie", expanded=True):
            st.markdown("""
            **Définition complète :**
            La gestion du temps est l'ensemble des processus, outils et techniques permettant d'organiser et de planifier la répartition du temps 
            entre différentes activités pour atteindre des objectifs spécifiques de manière efficace et efficiente.
            
            **Théorie :**
            - **Loi de Pareto :** 80% des résultats proviennent de 20% des efforts
            - **Loi de Parkinson :** Le travail s'étend pour remplir le temps disponible
            - **Matrice d'Eisenhower :** Classification des tâches selon l'urgence et l'importance
            - **Méthode Pomodoro :** Travail par intervalles de 25 minutes
            - **Loi de Carlson :** Le travail continué est plus efficace que le travail interrompu
            
            **Principes clés :**
            1. **Fixation d'objectifs SMART** (Spécifiques, Mesurables, Atteignables, Réalistes, Temporels)
            2. **Priorisation efficace** (urgent/important)
            3. **Planification réaliste** (estimation du temps nécessaire)
            4. **Délégation appropriée** (savoir déléguer)
            5. **Élimination des distracteurs** (gestion des interruptions)
            
            **Bénéfices :**
            - Productivité accrue
            - Stress réduit
            - Meilleur équilibre vie professionnelle/personnelle
            - Atteinte des objectifs
            - Satisfaction personnelle accrue
            """)

        st.subheader("📝 Test – Situations réelles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.radio("1. Plusieurs tâches aujourd'hui :", 
                         ["Prioriser et planifier", "Tout faire d'un coup", "Ignorer certaines tâches"], 
                         key="t1")
            q3 = st.radio("3. Tâche urgente :", 
                         ["Réorganiser ton planning", "Stresser et tout faire", "Reporter les autres tâches"], 
                         key="t3")
            q5 = st.radio("5. Planifier sa journée :", 
                         ["Avec un agenda ou calendrier", "Mentalement", "Sans plan"], 
                         key="t5")
            q7 = st.radio("7. Objectifs long terme :", 
                         ["Attribuer du temps à chaque objectif", "Tout faire en même temps", "Ne rien planifier"], 
                         key="t7")
            q9 = st.radio("9. Collaboration :", 
                         ["Coordonner et planifier ensemble", "Faire chaque tâche seul", "Attendre que quelqu'un te dise quoi faire"], 
                         key="t9")
            q11 = st.radio("11. Tâche répétitive :", 
                          ["Programmer des plages horaires et pauses", "Tout faire d'un coup", "Reporter souvent"], 
                          key="t11")
            q13 = st.radio("13. Délégation :", 
                          ["Attribuer à la personne compétente", "Tout garder pour toi", "Ignorer la tâche"], 
                          key="t13")
            q15 = st.radio("15. Fin de journée chargée :", 
                          ["Réviser et ajuster le planning", "Tout laisser de côté", "Travailler jusqu'à épuisement"], 
                          key="t15")
            
        with col2:
            q2 = st.radio("2. Avant un projet important :", 
                         ["Prépares un plan détaillé", "Commences sans plan", "Demandes aux autres de décider"], 
                         key="t2")
            q4 = st.radio("4. Procrastination :", 
                         ["Diviser la tâche en petites étapes", "Remettre encore", "Ignorer le travail"], 
                         key="t4")
            q6 = st.radio("6. Interruption fréquente :", 
                         ["Bloquer du temps pour tâches importantes", "Laisser les interruptions guider la journée", "Ignorer les interruptions"], 
                         key="t6")
            q8 = st.radio("8. Retard sur une tâche :", 
                         ["Réorganiser tes priorités", "Paniquer et stresser", "Abandonner la tâche"], 
                         key="t8")
            q10 = st.radio("10. Temps mal utilisé :", 
                          ["Analyser et améliorer ton emploi du temps", "Continuer comme ça", "Blâmer les autres"], 
                          key="t10")
            q12 = st.radio("12. Journée avec imprévus :", 
                          ["Adapter le planning et priorités", "Tout abandonner", "Se laisser envahir par le stress"], 
                          key="t12")
            q14 = st.radio("14. Perte de temps :", 
                          ["Analyser et réorganiser", "Continuer sans changement", "Râler sans agir"], 
                          key="t14")
        
        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

        bonnes = [
            "Prioriser et planifier", 
            "Prépares un plan détaillé", 
            "Réorganiser ton planning",
            "Diviser la tâche en petites étapes", 
            "Avec un agenda ou calendrier", 
            "Bloquer du temps pour tâches importantes",
            "Attribuer du temps à chaque objectif", 
            "Réorganiser tes priorités", 
            "Coordonner et planifier ensemble",
            "Analyser et améliorer ton emploi du temps", 
            "Programmer des plages horaires et pauses", 
            "Adapter le planning et priorités",
            "Attribuer à la personne compétente", 
            "Analyser et réorganiser", 
            "Réviser et ajuster le planning"
        ]

        videos = ["https://www.youtube.com/watch?v=oTugjssqOT0"]
        resources = "📚 [Guide complet de gestion du temps](https://example.com)"

    # ---------------- Gestion des conflits & EQ ----------------
    elif skill == "Gestion des conflits & Intelligence émotionnelle":
        st.header("🤝 Gestion des conflits & Intelligence émotionnelle")
        
        with st.expander("📖 Définition complète et théorie", expanded=True):
            st.markdown("""
            **Définition complète :**
            - **Gestion des conflits :** Processus de résolution des désaccords de manière constructive, en trouvant des solutions mutuellement acceptables
            - **Intelligence émotionnelle (IE) :** Capacité à identifier, comprendre, gérer et utiliser ses propres émotions et celles des autres de manière positive
            
            **Théorie :**
            - **Modèle de Goleman :** 5 composantes de l'IE (conscience de soi, autorégulation, motivation, empathie, compétences sociales)
            - **Modèle de Thomas-Kilmann :** 5 styles de gestion de conflits (compétition, collaboration, compromis, évitement, accommodation)
            - **Triangle du conflit de Fisher :** Positions, intérêts, besoins
            - **Communication non-violente (CNV) :** Méthode de Marshall Rosenberg
            
            **Composantes de l'Intelligence Émotionnelle :**
            1. **Conscience de soi :** Reconnaître ses émotions et leur impact
            2. **Autorégulation :** Gérer ses émotions de manière appropriée
            3. **Motivation :** Utiliser les émotions pour atteindre des objectifs
            4. **Empathie :** Comprendre les émotions des autres
            5. **Compétences sociales :** Gérer les relations efficacement
            
            **Styles de gestion des conflits :**
            - **Collaboration :** Recherche de solutions gagnant-gagnant
            - **Compromis :** Chaque partie fait des concessions
            - **Compétition :** Affirmation de ses besoins sans compromis
            - **Accommodation :** Satisfaire les besoins de l'autre
            - **Évitement :** Ne pas traiter le conflit
            """)

        st.subheader("📝 Test – Situations réelles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.radio("1. Un collègue critique ton travail :", 
                         ["Écouter calmement et répondre avec faits", "Répondre agressivement", "Ignorer et se fâcher"], 
                         key="c1")
            q3 = st.radio("3. Colère pendant un désaccord :", 
                         ["Respirer et reformuler calmement", "Exploser", "Quitter la conversation"], 
                         key="c3")
            q5 = st.radio("5. Conflit entre collègues :", 
                         ["Faciliter une discussion et chercher une solution", "Prendre parti", "Laisser faire"], 
                         key="c5")
            q7 = st.radio("7. Personne frustrée mais silencieuse :", 
                         ["Identifier et discuter de ses besoins", "Ne rien faire", "Lui reprocher"], 
                         key="c7")
            q9 = st.radio("9. Idée volée :", 
                         ["Expliquer calmement et reconnaître contributions", "Confronter agressivement", "Ne rien dire"], 
                         key="c9")
            q11 = st.radio("11. Conflit prolongé :", 
                          ["Organiser une médiation", "Ignorer le conflit", "Accuser les autres"], 
                          key="c11")
            
        with col2:
            q2 = st.radio("2. Membre de l'équipe stressé :", 
                         ["Proposer ton aide et comprendre", "Te concentrer sur ton travail", "Dire de se calmer"], 
                         key="c2")
            q4 = st.radio("4. Feedback négatif :", 
                         ["Préparer un message constructif et empathique", "Critiquer directement", "Éviter le sujet"], 
                         key="c4")
            q6 = st.radio("6. Discussion tendue client :", 
                         ["Rester calme et écouter attentivement", "Répondre émotionnellement", "Ignorer"], 
                         key="c6")
            q8 = st.radio("8. Compliment reçu :", 
                         ["Accepter poliment et remercier", "Refuser ou minimiser", "Ignorer"], 
                         key="c8")
            q10 = st.radio("10. Réunion tendue :", 
                          ["Chercher consensus et compromis", "Imposer ton point de vue", "Rester silencieux"], 
                          key="c10")
            q12 = st.radio("12. Émotions personnelles :", 
                          ["Prendre du recul et gérer ses émotions", "Ignorer", "Réagir impulsivement"], 
                          key="c12")
        
        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]

        bonnes = [
            "Écouter calmement et répondre avec faits", 
            "Proposer ton aide et comprendre", 
            "Respirer et reformuler calmement",
            "Préparer un message constructif et empathique", 
            "Faciliter une discussion et chercher une solution",
            "Rester calme et écouter attentivement", 
            "Identifier et discuter de ses besoins", 
            "Accepter poliment et remercier",
            "Expliquer calmement et reconnaître contributions", 
            "Chercher consensus et compromis", 
            "Organiser une médiation",
            "Prendre du recul et gérer ses émotions"
        ]
        videos = ["https://www.youtube.com/watch?v=d6A2Cp9dONA"]
        resources = "📚 [Communication non-violente et gestion des conflits](https://example.com)"

    # ---------------- Adaptation au changement ----------------
    elif skill == "Adaptation au changement":
        st.header("🔄 Adaptation au changement")
        
        with st.expander("📖 Définition complète et théorie", expanded=True):
            st.markdown("""
            **Définition complète :**
            L'adaptation au changement est la capacité d'ajuster ses comportements, attitudes, compétences et stratégies face à des situations nouvelles, 
            imprévues ou en évolution constante. Elle implique la flexibilité cognitive et comportementale, la résilience et l'ouverture d'esprit.
            
            **Théorie :**
            - **Modèle de transition de Bridges :** 3 phases (fin, zone neutre, nouveau début)
            - **Théorie de la résilience :** Capacité à rebondir face aux adversités
            - **Modèle ADKAR :** 5 étapes (Conscience, Désir, Connaissance, Capacité, Renforcement)
            - **Apprentissage continu :** Nécessité de mise à jour constante des compétences
            
            **Compétences clés pour l'adaptation :**
            1. **Flexibilité mentale :** Capacité à changer de perspective
            2. **Résilience émotionnelle :** Gérer l'incertitude et le stress
            3. **Curiosité et apprentissage :** Ouverture aux nouvelles idées
            4. **Prise de risque calculée :** Sortir de sa zone de confort
            5. **Optimisme réaliste :** Voir les opportunités dans le changement
            
            **Étapes du processus d'adaptation :**
            1. **Reconnaissance :** Accepter la nécessité du changement
            2. **Exploration :** Rechercher de nouvelles façons de faire
            3. **Expérimentation :** Tester de nouvelles approches
            4. **Intégration :** Adopter les changements réussis
            5. **Optimisation :** Améliorer continuellement
            
            **Facteurs facilitant l'adaptation :**
            - Soutien social et réseau
            - Compétences en résolution de problèmes
            - Confiance en ses capacités
            - Vision claire des bénéfices du changement
            """)

        st.subheader("📝 Test – Situations réelles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.radio("1. Nouveau logiciel au travail :", 
                         ["Apprendre rapidement et l'utiliser", "Se plaindre et résister", "Ignorer"], 
                         key="ch1")
            q3 = st.radio("3. Nouvelle méthode collègue :", 
                         ["Observer et s'inspirer", "Critiquer", "Ignorer"], 
                         key="ch3")
            q5 = st.radio("5. Problème imprévu :", 
                         ["Analyser rapidement et s'adapter", "Paniquer", "Attendre"], 
                         key="ch5")
            q7 = st.radio("7. Nouvelle compétence à apprendre :", 
                         ["Accepter et pratiquer", "Refuser", "Reporter"], 
                         key="ch7")
            q9 = st.radio("9. Nouveau membre équipe :", 
                         ["S'adapter à son style", "Ignorer", "Imposer votre méthode"], 
                         key="ch9")
            q11 = st.radio("11. Nouveau client exige ajustements :", 
                          ["Adapter rapidement", "Se plaindre", "Reporter"], 
                          key="ch11")
            q13 = st.radio("13. Nouvelle technologie :", 
                          ["Se former et utiliser", "Ignorer", "Critiquer"], 
                          key="ch13")
            q15 = st.radio("15. Objectifs perso changent :", 
                          ["S'adapter et ajuster ses actions", "Ignorer", "Se plaindre"], 
                          key="ch15")
            
        with col2:
            q2 = st.radio("2. Équipe change de projet :", 
                         ["S'adapter et contribuer positivement", "Se lamenter", "Refuser le changement"], 
                         key="ch2")
            q4 = st.radio("4. Nouvelle politique :", 
                         ["Comprendre et ajuster vos priorités", "Ignorer", "Se mettre en colère"], 
                         key="ch4")
            q6 = st.radio("6. Manager change objectifs :", 
                         ["Accepter et ajuster", "Résister", "Reporter"], 
                         key="ch6")
            q8 = st.radio("8. Tâche complexe :", 
                         ["Rechercher des solutions et s'adapter", "Se plaindre", "Abandonner"], 
                         key="ch8")
            q10 = st.radio("10. Changements fréquents :", 
                          ["Rester flexible et positif", "Se décourager", "Se bloquer"], 
                          key="ch10")
            q12 = st.radio("12. Priorités changent :", 
                          ["Réorganiser et rester productif", "Ignorer et stresser", "Tout abandonner"], 
                          key="ch12")
            q14 = st.radio("14. Projet échoue :", 
                          ["Apprendre et recommencer", "Se décourager", "Blâmer les autres"], 
                          key="ch14")
        
        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

        bonnes = [
            "Apprendre rapidement et l'utiliser", 
            "S'adapter et contribuer positivement", 
            "Observer et s'inspirer",
            "Comprendre et ajuster vos priorités", 
            "Analyser rapidement et s'adapter", 
            "Accepter et ajuster",
            "Accepter et pratiquer", 
            "Rechercher des solutions et s'adapter", 
            "S'adapter à son style",
            "Rester flexible et positif", 
            "Adapter rapidement", 
            "Réorganiser et rester productif",
            "Se former et utiliser", 
            "Apprendre et recommencer", 
            "S'adapter et ajuster ses actions"
        ]
        
        videos = ["https://www.youtube.com/watch?v=qYK8Oqx7mro"]
        resources = "📚 [Résilience et adaptabilité](https://example.com)"

    # ---------------- Intelligence financière ----------------
    elif skill == "Intelligence financière":
        st.header("💰 Intelligence financière")
        
        with st.expander("📖 Définition complète et théorie", expanded=True):
            st.markdown("""
            **Définition complète :**
            L'intelligence financière est la capacité à comprendre et appliquer les principes financiers pour prendre des décisions éclairées 
            concernant la gestion de l'argent, l'investissement, la planification financière et la création de richesse.
            
            **Théorie :**
            - **Éducation financière :** Connaissance des concepts financiers de base
            - **Planification financière :** Processus de gestion des finances pour atteindre des objectifs
            - **Investissement :** Allocation de ressources pour générer des rendements
            - **Gestion des risques :** Protection contre les pertes financières
            
            **Piliers de l'intelligence financière :**
            1. **Budgétisation :** Contrôle des revenus et dépenses
            2. **Épargne :** Mise de côté systématique
            3. **Investissement :** Croissance du capital
            4. **Gestion de la dette :** Contrôle et réduction des dettes
            5. **Planification :** Objectifs financiers à court, moyen et long terme
            
            **Concepts clés :**
            - **Intérêts composés :** Effet boule de neige des intérêts
            - **Diversification :** Répartition des risques
            - **Liquidité :** Disponibilité des fonds
            - **Inflation :** Perte de pouvoir d'achat
            - **Rendement vs risque :** Relation entre gain potentiel et risque
            
            **Niveaux d'intelligence financière :**
            1. **Survie :** Gestion des besoins immédiats
            2. **Stabilité :** Réserve d'urgence et budget équilibré
            3. **Indépendance :** Investissements générant des revenus passifs
            4. **Liberté :** Richesse suffisante pour vivre sans travailler
            5. **Abondance :** Richesse permettant de contribuer significativement
            
            **Outils d'analyse financière :**
            - Budget personnel
            - Tableau des flux de trésorerie
            - Bilan personnel
            - Ratios financiers (dette/revenu, épargne/revenu)
            """)

        st.subheader("📝 Test – Situations réelles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.radio("1. Tu veux économiser pour un projet important :", 
                         ["Établir un budget et suivre ses dépenses", "Acheter impulsivement", "Ignorer le projet"], 
                         key="f1")
            q3 = st.radio("3. Une dette importante survient :", 
                         ["Planifier un remboursement progressif", "Ignorer et espérer", "Augmenter les dépenses"], 
                         key="f3")
            q5 = st.radio("5. Pour gérer les finances quotidiennes :", 
                         ["Suivre les revenus et dépenses", "Ne rien suivre", "Emprunter régulièrement"], 
                         key="f5")
            q7 = st.radio("7. Objectifs financiers à long terme :", 
                         ["Épargner régulièrement et planifier", "Ignorer les objectifs", "Vivre au jour le jour"], 
                         key="f7")
            q9 = st.radio("9. Revenus fluctuants :", 
                         ["Ajuster budget et dépenses", "Dépenses fixes sans adaptation", "Arrêter d'épargner"], 
                         key="f9")
            q11 = st.radio("11. Une opportunité d'investissement sûre :", 
                          ["Analyser et décider avec prudence", "Se précipiter", "Ignorer l'opportunité"], 
                          key="f11")
            q13 = st.radio("13. Compréhension des impôts :", 
                          ["Se renseigner et optimiser légalement", "Ignorer", "Éviter de payer"], 
                          key="f13")
            q15 = st.radio("15. Équilibre dépenses-épargne :", 
                          ["Prioriser l'épargne et planifier les dépenses", "Tout dépenser", "Ne pas planifier"], 
                          key="f15")
            
        with col2:
            q2 = st.radio("2. Tu reçois un revenu supplémentaire :", 
                         ["Investir ou épargner", "Tout dépenser", "Ne rien faire"], 
                         key="f2")
            q4 = st.radio("4. Tu veux investir :", 
                         ["Chercher des informations et diversifier", "Mettre tout dans un seul produit risqué", "Ne pas investir"], 
                         key="f4")
            q6 = st.radio("6. Face à une dépense imprévue :", 
                         ["Utiliser une épargne d'urgence", "Endetter davantage", "Ignorer le problème"], 
                         key="f6")
            q8 = st.radio("8. Comprendre les finances personnelles :", 
                         ["Apprendre les bases et suivre son budget", "Ignorer les finances", "Se fier aux autres sans comprendre"], 
                         key="f8")
            q10 = st.radio("10. Pour éviter le stress financier :", 
                          ["Planifier, suivre et investir intelligemment", "Tout dépenser rapidement", "Ne rien planifier"], 
                          key="f10")
            q12 = st.radio("12. Dépenses mensuelles excessives :", 
                          ["Réduire et réorganiser le budget", "Continuer à dépenser", "Emprunter"], 
                          key="f12")
            q14 = st.radio("14. Éducation financière :", 
                          ["Apprendre et appliquer les concepts", "Ignorer", "Se fier aux rumeurs"], 
                          key="f14")
        
        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

        bonnes = [
            "Établir un budget et suivre ses dépenses",
            "Investir ou épargner",
            "Planifier un remboursement progressif",
            "Chercher des informations et diversifier",
            "Suivre les revenus et dépenses",
            "Utiliser une épargne d'urgence",
            "Épargner régulièrement et planifier",
            "Apprendre les bases et suivre son budget",
            "Ajuster budget et dépenses",
            "Planifier, suivre et investir intelligemment",
            "Analyser et décider avec prudence",
            "Réduire et réorganiser le budget",
            "Se renseigner et optimiser légalement",
            "Apprendre et appliquer les concepts",
            "Prioriser l'épargne et planifier les dépenses",
        ]

        # VIDÉO UNIQUE pour l'intelligence financière
        videos = ["https://www.youtube.com/watch?v=h4ndSKf6EmM"]
        resources = ""  # Ressources supprimées comme demandé

    # ---------------- Résolution de problèmes ----------------
    elif skill == "Résolution de problèmes":
        st.header("🔍 Résolution de problèmes")
        
        with st.expander("📖 Définition complète et théorie", expanded=True):
            st.markdown("""
            **Définition complète :**
            La résolution de problèmes est un processus mental qui consiste à identifier, analyser et résoudre des difficultés ou des obstacles 
            de manière systématique et efficace. C'est une compétence cognitive fondamentale qui combine pensée critique, créativité et prise de décision.
            
            **Théorie :**
            - **Processus de résolution de problèmes :** 6 étapes clés (identification, analyse, génération, évaluation, mise en œuvre, évaluation)
            - **Pensée divergente vs convergente :** Générer des idées vs sélectionner la meilleure solution
            - **Heuristiques et algorithmes :** Règles pratiques vs procédures systématiques
            - **Biais cognitifs :** Obstacles à la résolution efficace de problèmes
            
            **Étapes du processus de résolution de problèmes :**
            1. **Identification du problème :** Définir clairement ce qui doit être résolu
            2. **Analyse du problème :** Comprendre les causes, contraintes et implications
            3. **Génération de solutions :** Brainstorming de plusieurs options possibles
            4. **Évaluation des solutions :** Analyser les avantages/inconvénients de chaque option
            5. **Sélection et mise en œuvre :** Choisir et appliquer la meilleure solution
            6. **Évaluation des résultats :** Vérifier l'efficacité et apprendre pour l'avenir
            
            **Techniques de résolution de problèmes :**
            - **Diagramme d'Ishikawa (5M) :** Analyse des causes racines
            - **Méthode des 5 pourquoi :** Recherche de la cause fondamentale
            - **Matrice de décision :** Évaluation systématique des options
            - **Pensée latérale :** Approches créatives et non conventionnelles
            - **Analyse SWOT :** Forces, Faiblesses, Opportunités, Menaces
            
            **Compétences associées :**
            - Pensée critique et analytique
            - Créativité et innovation
            - Prise de décision
            - Gestion des risques
            - Communication claire
            """)

        st.subheader("📝 Test – Situations réelles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.radio("1. Problème technique récurrent :", 
                         ["Analyser la cause racine", "Appliquer des solutions temporaires", "Ignorer le problème"], 
                         key="rp1")
            q3 = st.radio("3. Objectif impossible à atteindre :", 
                         ["Décomposer en étapes réalisables", "Abandonner immédiatement", "Continuer sans changement"], 
                         key="rp3")
            q5 = st.radio("5. Deux solutions possibles :", 
                         ["Évaluer avantages/inconvénients de chaque", "Choisir au hasard", "Ne pas décider"], 
                         key="rp5")
            q7 = st.radio("7. Problème complexe avec plusieurs aspects :", 
                         ["Utiliser une approche structurée (ex: diagramme)", "Traiter au hasard", "Éviter le problème"], 
                         key="rp7")
            q9 = st.radio("9. Solution qui fonctionne partiellement :", 
                         ["Analyser pourquoi et améliorer", "Accepter telle quelle", "Tout recommencer à zéro"], 
                         key="rp9")
            q11 = st.radio("11. Problème sous contrainte de temps :", 
                          ["Prioriser l'essentiel et agir rapidement", "Paniquer et ne rien faire", "Ignorer les contraintes"], 
                          key="rp11")
            q13 = st.radio("13. Échec d'une solution :", 
                          ["Analyser l'échec et essayer autre chose", "Abandonner complètement", "Refaire exactement pareil"], 
                          key="rp13")
            
        with col2:
            q2 = st.radio("2. Nouveau problème sans précédent :", 
                         ["Rechercher des informations et comparer", "Paniquer et abandonner", "Improviser sans réfléchir"], 
                         key="rp2")
            q4 = st.radio("4. Blocage dans la réflexion :", 
                         ["Changer de perspective ou demander aide", "Insister sur la même approche", "Arrêter de travailler dessus"], 
                         key="rp4")
            q6 = st.radio("6. Problème affectant plusieurs personnes :", 
                         ["Consulter les parties prenantes", "Décider seul", "Laisser les autres régler"], 
                         key="rp6")
            q8 = st.radio("8. Solution créative mais risquée :", 
                         ["Évaluer les risques et planifier", "Rejeter par peur", "Foncer sans préparation"], 
                         key="rp8")
            q10 = st.radio("10. Problème mal défini :", 
                          ["Clarifier l'objectif et les contraintes", "Traiter sans comprendre", "Attendre plus d'informations"], 
                          key="rp10")
            q12 = st.radio("12. Solution idéale mais coûteuse :", 
                          ["Rechercher des alternatives moins chères", "Abandonner par manque de budget", "Dépenser sans compter"], 
                          key="rp12")
            q14 = st.radio("14. Problème résolu avec succès :", 
                          ["Documenter le processus pour l'avenir", "Passer au problème suivant", "Se féliciter et oublier"], 
                          key="rp14")
        
        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14]

        bonnes = [
            "Analyser la cause racine",
            "Rechercher des informations et comparer",
            "Décomposer en étapes réalisables",
            "Changer de perspective ou demander aide",
            "Évaluer avantages/inconvénients de chaque",
            "Consulter les parties prenantes",
            "Utiliser une approche structurée (ex: diagramme)",
            "Évaluer les risques et planifier",
            "Analyser pourquoi et améliorer",
            "Clarifier l'objectif et les contraintes",
            "Prioriser l'essentiel et agir rapidement",
            "Rechercher des alternatives moins chères",
            "Analyser l'échec et essayer autre chose",
            "Documenter le processus pour l'avenir"
        ]

        videos = ["https://www.youtube.com/watch?v=QFjqJeD_1Eo"]
        resources = "📚 [Techniques avancées de résolution de problèmes](https://example.com)"

    # ---------------- Leadership ----------------
    elif skill == "Leadership":
        st.header("👑 Leadership")
        
        with st.expander("📖 Définition complète et théorie", expanded=True):
            st.markdown("""
            **Définition complète :**
            Le leadership est l'art d'influencer, de motiver et de guider les individus ou les groupes vers l'atteinte d'objectifs communs. 
            C'est la capacité à inspirer confiance, à prendre des initiatives et à créer un environnement propice à la réussite collective.
            
            **Théorie :**
            - **Théories des traits :** Caractéristiques personnelles des leaders efficaces
            - **Théories comportementales :** Actions et comportements des leaders
            - **Théories contingentes :** Adaptation du style de leadership à la situation
            - **Théories transformationnelles :** Capacité à inspirer et transformer les autres
            - **Leadership situationnel de Hersey-Blanchard :** Adaptation au niveau de maturité des collaborateurs
            
            **Styles de leadership :**
            1. **Directif :** Donne des instructions claires et spécifiques
            2. **Participatif :** Implique l'équipe dans les décisions
            3. **Délégatif :** Fait confiance et donne de l'autonomie
            4. **Transformational :** Inspire et motive vers une vision commune
            5. **Serviteur :** Met les besoins des autres en premier
            6. **Charismatique :** Utilise son charisme pour influencer
            
            **Compétences clés du leader :**
            1. **Vision stratégique :** Voir l'avenir et tracer le chemin
            2. **Communication efficace :** Écouter, expliquer, convaincre
            3. **Décision :** Prendre des décisions éclairées et opportunes
            4. **Délégation :** Savoir confier des responsabilités
            5. **Motivation :** Inspirer et mobiliser les talents
            6. **Développement des autres :** Faire grandir son équipe
            7. **Intégrité :** Agir avec éthique et transparence
            8. **Résilience :** Gérer les pressions et les échecs
            
            **Leadership vs Management :**
            - **Management :** Administrer, contrôler, maintenir les systèmes
            - **Leadership :** Innover, inspirer, développer les personnes
            
            **Développement du leadership :**
            - Auto-réflexion et feedback
            - Mentorat et coaching
            - Expériences diversifiées
            - Formation continue
            - Réseautage stratégique
            """)

        st.subheader("📝 Test – Situations réelles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.radio("1. Nouveau projet à lancer :", 
                         ["Partager la vision et motiver l'équipe", "Donner des ordres précis", "Laisser l'équipe décider seule"], 
                         key="l1")
            q3 = st.radio("3. Membre d'équipe sous-performant :", 
                         ["Identifier les causes et coacher", "Critiquer publiquement", "Ignorer en espérant une amélioration"], 
                         key="l3")
            q5 = st.radio("5. Décision difficile à prendre :", 
                         ["Consulter l'équipe puis décider", "Décider seul rapidement", "Éviter de décider"], 
                         key="l5")
            q7 = st.radio("7. Conflit dans l'équipe :", 
                         ["Faciliter la résolution du conflit", "Prendre parti", "Laisser les gens régler seuls"], 
                         key="l7")
            q9 = st.radio("9. Objectif ambitieux à atteindre :", 
                         ["Décomposer et célébrer les petites victoires", "Faire pression sur l'équipe", "Réduire l'objectif immédiatement"], 
                         key="l9")
            q11 = st.radio("11. Échec d'un projet :", 
                          ["Analyser les leçons et responsabiliser", "Trouver un coupable", "Faire comme si rien n'était arrivé"], 
                          key="l11")
            q13 = st.radio("13. Talent prometteur dans l'équipe :", 
                          ["Lui donner des défis pour grandir", "Le garder à sa place", "Le considérer comme une menace"], 
                          key="l13")
            
        with col2:
            q2 = st.radio("2. Changement organisationnel majeur :", 
                         ["Communiquer clairement et rassurer", "Imposer le changement", "Cacher les informations"], 
                         key="l2")
            q4 = st.radio("4. Crise nécessitant une action rapide :", 
                         ["Prendre les commandes avec calme", "Paniquer avec l'équipe", "Attendre des instructions"], 
                         key="l4")
            q6 = st.radio("6. Feedback à donner à un collaborateur :", 
                         ["Donner un feedback constructif en privé", "Éviter le feedback difficile", "Critiquer devant l'équipe"], 
                         key="l6")
            q8 = st.radio("8. Tâche importante à déléguer :", 
                         ["Choisir la bonne personne et expliquer le pourquoi", "Donner à n'importe qui", "Garder pour soi par méfiance"], 
                         key="l8")
            q10 = st.radio("10. Réunion d'équipe improductive :", 
                          ["Redynamiser avec un objectif clair", "Laisser traîner la réunion", "Annuler les prochaines réunions"], 
                          key="l10")
            q12 = st.radio("12. Manque d'innovation dans l'équipe :", 
                          ["Créer un environnement safe pour les idées", "Critiquer le manque de créativité", "Imposer ses propres idées"], 
                          key="l12")
            q14 = st.radio("14. Développement de ta propre équipe :", 
                          ["Investir dans leur formation et croissance", "Se concentrer uniquement sur les résultats", "Les remplacer fréquemment"], 
                          key="l14")
        
        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14]

        bonnes = [
            "Partager la vision et motiver l'équipe",
            "Communiquer clairement et rassurer",
            "Identifier les causes et coacher",
            "Prendre les commandes avec calme",
            "Consulter l'équipe puis décider",
            "Donner un feedback constructif en privé",
            "Faciliter la résolution du conflit",
            "Choisir la bonne personne et expliquer le pourquoi",
            "Décomposer et célébrer les petites victoires",
            "Redynamiser avec un objectif clair",
            "Analyser les leçons et responsabiliser",
            "Créer un environnement safe pour les idées",
            "Lui donner des défis pour grandir",
            "Investir dans leur formation et croissance"
        ]

        videos = ["https://www.youtube.com/watch?v=XKUPDUDOBVo"]
        resources = "📚 [Développement du leadership et management](https://example.com)"

    # Bouton pour voir le résultat
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button(f"📊 ANALYSER MON SCORE {skill}", type="primary", use_container_width=True):
            # Vérifier si toutes les questions sont répondues
            unanswered = [i+1 for i, q in enumerate(questions) if q is None or q == ""]
            
            if unanswered:
                st.error(f"❌ Veuillez répondre aux questions suivantes : {', '.join(map(str, unanswered))}")
            else:
                # Calcul du score
                score = 0
                wrong_answers = []
                
                for i in range(len(questions)):
                    user_answer = questions[i]
                    correct_answer = bonnes[i]
                    
                    if user_answer == correct_answer:
                        score += 1
                    else:
                        wrong_answers.append({
                            'question': i+1,
                            'user_answer': user_answer,
                            'correct_answer': correct_answer
                        })
                
                total_questions = len(questions)
                score_percent = (score / total_questions) * 100

                # Affichage des résultats
                st.markdown("---")
                st.subheader(f"📈 RÉSULTATS : {skill}")
                
                # Score avec design amélioré
                st.markdown(f"""
                <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
                    <h1 style='color: #4CAF50; font-size: 48px; margin: 0;'>{score}/{total_questions}</h1>
                    <h3 style='color: #666; margin: 10px 0;'>{score_percent:.1f}% de réussite</h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Barre de progression colorée
                progress_color = "#4CAF50" if score_percent >= 70 else "#FF9800" if score_percent >= 40 else "#F44336"
                st.markdown(f"""
                <div style='width: 100%; background-color: #e0e0e0; border-radius: 5px; margin: 20px 0;'>
                    <div style='width: {score_percent}%; background-color: {progress_color}; height: 20px; border-radius: 5px;'></div>
                </div>
                """, unsafe_allow_html=True)
                
                # Interprétation détaillée
                st.markdown("### 📋 INTERPRÉTATION DE VOTRE SCORE")
                
                if score_percent <= 40:
                    st.error("**🏁 NIVEAU DÉBUTANT**")
                    st.markdown("""
                    <div style='background-color: #FFEBEE; padding: 20px; border-radius: 10px; border-left: 5px solid #F44336;'>
                    <h4 style='color: #D32F2F;'>Opportunités d'amélioration</h4>
                    <p>Vous commencez votre parcours dans cette compétence. C'est le moment idéal pour construire des bases solides !</p>
                    <h5>🎯 Actions recommandées :</h5>
                    <ul>
                        <li>Commencez par les concepts fondamentaux</li>
                        <li>Pratiquez dans des situations simples du quotidien</li>
                        <li>Suivez un cours ou une formation de base</li>
                        <li>Identifiez 1-2 points à améliorer en priorité</li>
                    </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                elif score_percent <= 70:
                    st.warning("**🌟 NIVEAU INTERMÉDIAIRE**")
                    st.markdown("""
                    <div style='background-color: #FFF3E0; padding: 20px; border-radius: 10px; border-left: 5px solid #FF9800;'>
                    <h4 style='color: #F57C00;'>Belles compétences de base !</h4>
                    <p>Vous avez développé de bonnes compétences, mais il reste des opportunités d'amélioration.</p>
                    <h5>🎯 Actions recommandées :</h5>
                    <ul>
                        <li>Consolidez vos points forts</li>
                        <li>Travaillez spécifiquement sur vos points faibles</li>
                        <li>Challengez-vous avec des situations plus complexes</li>
                        <li>Partagez vos connaissances avec des débutants</li>
                    </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                else:
                    st.success("**🏆 NIVEAU AVANCÉ**")
                    st.markdown("""
                    <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; border-left: 5px solid #4CAF50;'>
                    <h4 style='color: #388E3C;'>Excellente maîtrise !</h4>
                    <p>Vous démontrez une compréhension approfondie et une application pratique de cette compétence.</p>
                    <h5>🎯 Actions recommandées :</h5>
                    <ul>
                        <li>Enseignez à d'autres pour consolider vos connaissances</li>
                        <li>Cherchez des défis plus complexes et variés</li>
                        <li>Développez une expertise dans des aspects spécifiques</li>
                        <li>Devenez mentor pour des personnes moins expérimentées</li>
                    </ul>
                    </div>
                    """, unsafe_allow_html=True)

                # Détails des réponses
                with st.expander("📊 DÉTAIL DE VOS RÉPONSES", expanded=True):
                    st.markdown("### Analyse question par question")
                    
                    for i in range(total_questions):
                        user_ans = questions[i]
                        correct_ans = bonnes[i]
                        
                        col_a, col_b = st.columns([1, 4])
                        
                        with col_a:
                            if user_ans == correct_ans:
                                st.success(f"Q{i+1} : ✅")
                            else:
                                st.error(f"Q{i+1} : ❌")
                        
                        with col_b:
                            if user_ans == correct_ans:
                                st.markdown(f"**Votre réponse :** *{user_ans}* - **Correct !**")
                            else:
                                st.markdown(f"""
                                **Votre réponse :** *{user_ans}*  
                                **Bonne réponse :** **{correct_ans}**
                                """)

                # Analyse des erreurs
                if wrong_answers:
                    st.markdown("### 🔍 ANALYSE DE VOS ERREURS")
                    st.write(f"Vous avez fait {len(wrong_answers)} erreur(s). Voici les domaines à retravailler :")
                    
                    for error in wrong_answers:
                        st.info(f"**Question {error['question']}** : Vous avez répondu '{error['user_answer']}' alors que la réponse attendue était '{error['correct_answer']}'")

                # Ressources d'apprentissage
                st.markdown("---")
                st.subheader("🎓 RESSOURCES POUR PROGRESSER")
                
                # Vidéos
                if videos:
                    st.markdown("#### 🎥 VIDÉOS ÉDUCATIVES")
                    for idx, video_url in enumerate(videos, 1):
                        st.markdown(f"**Vidéo {idx}** - [Lien direct]({video_url})")
                        try:
                            st.video(video_url)
                        except:
                            st.warning(f"Impossible de charger la vidéo {idx}. Vous pouvez la visionner directement sur [YouTube]({video_url})")
                
                # Ressources supplémentaires (sauf pour intelligence financière)
                if skill != "Intelligence financière" and resources:
                    st.markdown("#### 📚 RESSOURCES COMPLÉMENTAIRES")
                    st.markdown(resources)
                
                # Plan d'action personnalisé
                st.markdown("#### 📝 PLAN D'ACTION PERSONNALISÉ")
                st.markdown(f"""
                **Pour {name}, voici votre plan d'amélioration :**
                
                1. **Cette semaine :** {f"Révisez les questions {', '.join([str(e['question']) for e in wrong_answers])}" if wrong_answers else "Consolidez vos connaissances avec une mise en pratique"}
                2. **Ce mois-ci :** Suivez au moins une des vidéos recommandées
                3. **Prochain trimestre :** Appliquez ces compétences dans 3 situations réelles différentes
                4. **Évaluation :** Reprenez ce test dans 1 mois pour mesurer votre progression
                """)
                
                # Bouton pour exporter les résultats
                st.markdown("---")
                st.subheader("💾 EXPORTER VOS RÉSULTATS")
                
                result_text = f"""
                RAPPORT D'ÉVALUATION - SOFT SKILLS
                ====================================
                
                Nom : {name}
                Compétence évaluée : {skill}
                Date : {st.session_state.date}
                
                RÉSULTATS :
                -----------
                Score : {score}/{total_questions}
                Pourcentage : {score_percent:.1f}%
                Niveau : {'Débutant' if score_percent <= 40 else 'Intermédiaire' if score_percent <= 70 else 'Avancé'}
                
                DÉTAIL DES RÉPONSES :
                --------------------
                """
                
                for i in range(total_questions):
                    result_text += f"\nQuestion {i+1}: "
                    if questions[i] == bonnes[i]:
                        result_text += f"CORRECT - {questions[i]}"
                    else:
                        result_text += f"INCORRECT - Votre réponse: {questions[i]} | Bonne réponse: {bonnes[i]}"
                
                result_text += f"""
                
                RECOMMANDATIONS :
                -----------------
                {'Priorisez l\'apprentissage des bases et pratiquez régulièrement.' if score_percent <= 40 else 
                  'Consolidez vos connaissances et challengez-vous avec des situations complexes.' if score_percent <= 70 else 
                  'Perfectionnez vos compétences et partagez vos connaissances.'}
                
                Prochain test recommandé : Dans 1 mois
                """
                
                st.download_button(
                    label="📥 Télécharger le rapport complet",
                    data=result_text,
                    file_name=f"Rapport_{skill}_{name.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )

else:
    st.info("👈 **Veuillez entrer votre nom pour commencer l'évaluation**")
    st.markdown("""
    <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px;'>
    <h4 style='color: #1565C0;'>💡 À propos de cette application</h4>
    <p>Cette application vous permet d'évaluer et d'améliorer vos compétences comportementales (soft skills) essentielles pour réussir dans le monde professionnel et personnel.</p>
    <ul>
        <li><strong>7 compétences</strong> disponibles</li>
        <li><strong>Tests pratiques</strong> basés sur des situations réelles</li>
        <li><strong>Ressources personnalisées</strong> selon votre niveau</li>
        <li><strong>Suivi de progression</strong> avec rapports détaillés</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>© 2024 Soft Skills Assessment App | Développé avec ❤️ et Streamlit</p>
    <p><small>Les résultats sont indicatifs et visent à aider votre développement personnel</small></p>
</div>
""", unsafe_allow_html=True)