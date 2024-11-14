from django.shortcuts import render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from myapp.models import DocumentComparison

def index(request):
    return render(request, 'index.html')

def highlight_common_words(text1, text2):
    # Tokenize dan buat set kata dari kedua dokumen
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    # Temukan kata-kata yang sama
    common_words = words1.intersection(words2)
    
    # Ganti kata-kata yang sama dengan versi yang diberi warna merah
    highlighted_text1 = ' '.join(f'<span style="color: red;">{word}</span>' if word in common_words else word for word in text1.split())
    highlighted_text2 = ' '.join(f'<span style="color: red;">{word}</span>' if word in common_words else word for word in text2.split())
    
    return highlighted_text1, highlighted_text2

def calculate_similarity(request):
    if request.method == 'POST':
        # Ambil teks dokumen dari form
        doc1 = request.POST.get('document1')
        doc2 = request.POST.get('document2')

        # Lakukan perhitungan TF-IDF dan Cosine Similarity
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([doc1, doc2])
        similarity_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

        # Soroti kata-kata yang sama
        highlighted_doc1, highlighted_doc2 = highlight_common_words(doc1, doc2)

        # Simpan hasil ke database
        comparison = DocumentComparison(document1=doc1, document2=doc2, similarity_score=similarity_score)
        comparison.save()

        # Kirim hasil ke template
        return render(request, 'index.html', {
            'similarity_score': similarity_score,
            'highlighted_doc1': highlighted_doc1,
            'highlighted_doc2': highlighted_doc2
        })

