# --- COEFFICIENTS ET CRITÈRES (VOS PRIORITÉS) ---
# Le total des coefficients est de 42 (8 + 10 + 7 + 7 + 10)
COEFFICIENTS = {
    "Intimité et Connexion Émotionnelle": 8,
    "Visions de la Famille et Éducation": 10,
    "Projets Financiers et Investissement Commun": 7,
    "Attractivité Physique de la Personne": 7,
    "Qualités Relationnelles et Fondamentales": 10
}

SCORE_MAX_TOTAL = sum(COEFFICIENTS.values()) * 10 # 42 * 10 = 420

def calculer_score_affinite(nom_partenaire, notes):
    """
    Calcule le score d'affinité pondéré basé sur les coefficients définis.

    :param nom_partenaire: Nom de la personne évaluée (str).
    :param notes: Liste des 5 notes attribuées (doit être dans l'ordre des COEFFICIENTS).
    :return: Score total pondéré et pourcentage d'affinité.
    """
    score_pondere_total = 0
    
    # Vérification que le nombre de notes est correct
    if len(notes) != len(COEFFICIENTS):
        print("Erreur : Vous devez fournir exactement 5 notes.")
        return None, None

    # Création d'une liste de couples (critère, coefficient, note)
    criteres_notes = list(zip(COEFFICIENTS.keys(), COEFFICIENTS.values(), notes))
    
    # Affichage du détail du calcul
    print(f"\n--- Détail du calcul pour {nom_partenaire} ---")
    
    for critere, coeff, note in criteres_notes:
        # Assurez-vous que la note est entre 1 et 10
        if not (1 <= note <= 10):
            print(f"Attention : La note '{critere}' ({note}) est hors de la plage 1-10.")
            note = max(1, min(10, note)) # Limite la note pour le calcul
            
        score_pondere_critere = note * coeff
        score_pondere_total += score_pondere_critere
        print(f"{critere:45s} | Note: {note:2d} | Coeff: {coeff:2d} | Score: {score_pondere_critere:3d}")

    # Calcul du pourcentage d'affinité
    pourcentage_affinite = (score_pondere_total / SCORE_MAX_TOTAL) * 100
    
    return score_pondere_total, pourcentage_affinite

# --- EXEMPLES D'UTILISATION (VOS DONNÉES) ---

# Notes de la Partenaire A (59.05%)
# Ordre : Intimité(8), Famille(10), Finance(7), Physique(7), Qualités(10)
notes_partenaire_A = [6, 3, 4, 6, 10]
score_A, pourcentage_A = calculer_score_affinite("Partenaire A", notes_partenaire_A)

# Notes de Safa (63.81%)
# Ordre : Intimité(8), Famille(10), Finance(7), Physique(7), Qualités(10)
notes_safa = [5, 7, 6, 8, 6]
score_safa, pourcentage_safa = calculer_score_affinite("Safa", notes_safa)

# --- AFFICHAGE DES RÉSULTATS FINAUX ---

print("\n=============================================")
if score_A is not None:
    print(f"**Score final Partenaire A : {score_A}/{SCORE_MAX_TOTAL} ({pourcentage_A:.2f}%)**")

print("\n---------------------------------------------")

if score_safa is not None:
    print(f"**Score final Safa : {score_safa}/{SCORE_MAX_TOTAL} ({pourcentage_safa:.2f}%)**")
print("=============================================")

