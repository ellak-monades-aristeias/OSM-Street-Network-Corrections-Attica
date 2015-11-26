### Επεξεργασία δεδομένων του OpenStreetMap Project για χρήση από εφαρμογές GIS - Μέρος Α’
**Πιλοτική Εφαρμογή στην Περιφέρεια Αττικής (πλην Νήσων) _(OSM-Street-Network-Corrections-Attica)_**

Το OpenStreetMap Project παρέχει δεδομένα οδικού δικτύου με εκτενή γεωγραφική κάλυψη που μπορούν να εξυπηρετήσουν πολλαπλές ανάγκες. Η λεπτομέρεια των δεδομένων καθώς και η διαρκής ενημέρωσή τους από μία ευρεία κοινότητα χρηστών παρέχουν ένα πολύ καλό υπόβαθρο για εφαρμογές που σχετίζονται με οδικά συγκοινωνιακά δίκτυα.

Ωστόσο, στην πρωτογενή τους μορφή τα δεδομένα αυτά δεν μπορούν να χρησιμοποιηθούν άμεσα από αρκετές εφαρμογές GIS, όπως εφαρμογές πλοήγησης, εύρεσης βέλτιστης διαδρομής κλπ., λόγω ορισμένων αδυναμιών που παρουσιάζουν, όπως:

1. Μη ύπαρξη τοπολογικών κόμβων (nodes) στις περισσότερες διασταυρώσεις των αξόνων.
2. Ατέλειες και ασυνέχειες της κατηγοριοποίησης των οδικών αξόνων.

Στόχος του παρόντος έργου είναι η αντιμετώπιση των προβλημάτων αυτών, ώστε να καταστεί το οδικό δίκτυο του OSM περισσότερο αξιοποιήσιμο από εφαρμογές GIS, κάνοντας τις λιγότερες δυνατές διορθωτικές επεμβάσεις (editing). Για τον λόγο αυτό καταρτίστηκε εξειδικευμένη μεθοδολογία, υποβοηθούμενη από customization scripts, μέσα στο περιβάλλον του ελεύθερου open-source λογισμικού QGIS και εφαρμόστηκε πιλοτικά στην Περιφέρεια Αττικής.

Υπάρχουν πολλά ακόμη που μπορούν να γίνουν ώστε να καταστεί ένα οδικό δίκτυο ακόμη πιο αξιοποιήσιμο από εφαρμογές GIS (όπως λεπτομερέστερη κατηγοριοποίηση των τόξων του δικτύου, εισαγωγή ειδικών περιορισμών κίνησης, τυποποίηση αναγραφών ονομασιών οδών κ.α.), εντούτοις σκοπός του παρόντος έργου είναι η αντιμετώπιση των δύο κυριότερων αδυναμιών που προαναφέρθηκαν.

Για περισσότερες πληροφορίες, παρακαλώ δείτε το [Wiki Page](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/wiki). Αν θέλετε, παρακολουθήστε το [προωθητικό βίντεο](https://www.youtube.com/watch?v=F8HNpRvpiGg) του έργου.

Μπορείτε να καταχωρείτε ως [issues](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/issues) όποιες βελτιώσεις, δυσλειτουργίες, προτάσεις κλπ. έχετε εντοπίσει σχετικά με το έργο αυτό.

Δείτε επίσης το έργο "Επεξεργασία δεδομένων του OpenStreetMap Project για χρήση από εφαρμογές GIS - Μέρος Β’: Επέκταση στην υπόλοιπη Ελλάδα ([OSM-Street-Network-Corrections-Greece](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Greece))", το οποίο αποτελεί επέκταση εφαρμογής του παρόντος.

**Παραδοτέα**

Τα παραδοτέα αρχεία του έργου βρίσκονται στους εξής συνδέσμους:

|       |                          **Παραδοτέο**                            |**URL**|
|:-----:|:------------------------------------------------------------------|:-----:|
|   1   |Καταγραφή διαδικασιών|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/OSM_Street_Network_Corrections_Reports.7z|
|   2   |Scripts παραμετροποίησης|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/Script_Convert_Greek_to_Latin_ELOT743.7z|
|   3   |Shapefile Αττικής σε WGS'84|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/roads_corrected_wgs84_attiki.7z|
|   4   |Shapefile Αττικής σε ΕΓΣΑ'87|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/roads_corrected_ggrs87_attiki.7z|

Μπορείτε να [κατεβάσετε και από Dropbox τα παραδοτέα αρχεία](https://www.dropbox.com/sh/gnx81f1zytrbfdq/AACqHRXdpPdOy_GUzlT91JXGa?dl=0) του έργου. _Ορισμένα αρχεία λόγω του μεγέθους τους δεν στάθηκε δυνατόν να ανέβουν στο αποθετήριο του έργου._

Δείτε εδώ αναλυτικότερες [πληροφορίες για τα Παραδοτέα](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/wiki/Deliverables).

**Το υλικό του έργου αυτού διατίθεται υπό τις Άδειες:**
- CC-BY-SA 4.0: Αρχεία διαδικασιών, πινάκων, κειμένων κλπ.
- EUPL 1.1: Scripts παραμετροποίησης
- ODbL 1.0: Χαρτογραφικά δεδομένα (shapefiles) από OSM (πρωτογενή αρχεία) & διορθωμένα παράγωγα αυτών

**Σε ποιούς απευθύνεται - Κοινότητες Χρηστών - Προγραμματιστών (Developers)**

Χρήστες GIS ασχολούμενοι με εφαρμογές πλοήγησης, εύρεσης βέλτιστης διαδρομής κλπ., τόσο για εμπορικούς όσο και για ερευνητικούς σκοπούς. Τελικοί χρήστες των επεξεργασμένων δεδομένων ή ενδιαφερόμενοι να αξιοποιήσουν την παρεχόμενη τεχνογνωσία για δική τους χρήση.

Τεκμηρίωση για τη διαδικασία παρέχεται στα pdf αρχεία:
* **Διαδικασία_Διορθώσεων_OSM_QGIS.pdf**: Πλήρης καταγραφή διαδικασίας & εργασιών για developers και χρήστες που ενδιαφέρονται να την εφαρμόσουν, τροποποιήσουν, επεκτείνουν κλπ.
* **Διαδικασία_Διορθώσεων_OSM_Simple.pdf**: Συνοπτικές οδηγίες για απλούς χρήστες.

Τα παραπάνω αρχεία βρίσκονται στο archive: [_OSM_Street_Network_Corrections_Reports.7z_](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/OSM_Street_Network_Corrections_Reports.7z)

**Overview**

The OpenStreetMap Project offers thorough street network data that can serve multiple needs. The detail of the data as well as its constant updating by a vast user community provide a very good background for applications concerning street networks.

However, this data in its raw form can't be used directly by a number of GIS applications, like navigation applications, shortest path algorithms etc., because of some inherent problems, such as:

1. Absence of topological nodes in most of the street junctions.
2. Imperfections and discontinuities of the street network classification.

The aim of this project is to rectify these problems, in order to make the OSM street network more useful for GIS applications, while making the least possible manual edits. To this end a special methodology was developed, supported by customization scripts, within the environment of free open-source QGIS software and was initially applied in the district of Attica (Athens), Greece.

The deliverables of this project can be [downloaded from Dropbox](https://www.dropbox.com/sh/gnx81f1zytrbfdq/AACqHRXdpPdOy_GUzlT91JXGa?dl=0). _Some files could not be uploaded to the project's repository due to their size._

You can also view the second part of this project ([OSM-Street-Network-Corrections-Greece](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Greece)), which extends its application to the whole of Greece.
