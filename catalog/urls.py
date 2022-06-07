from django.urls import path, include
from catalog import views
 #from django.contrib.auth.urls
urlpatterns = [
    
    #-------------------------------Home URL-------------------------------
    path('', views.index, name = 'index'),
    #_________________________________________________________________________________________
    
    
    #-------------------------------Gener URLS-------------------------------
    path('gener/', views.GenerListView.as_view(), name = 'geners'),
    #_________________________________________________________________________________________
    
    
    #-------------------------------Django Authentication URLS-------------------------------
    #Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    #_________________________________________________________________________________________
    
    
    # -------------------------------Book & BookInstances URLS-------------------------------
    path('books/', views.BookListView.as_view(), name = 'books'),
    # Url path to the user borrowed book page (only loged-in users can access).
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name = 'my-borrowed'),
    # All borrowed books page (only librarians can access).
    path('borrowedbooks/', views.AllLoanedBooksListView.as_view(), name = 'all-borrowed-books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name = 'book-detail'),
    # Renewal date page (Only librarians can access)
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name= 'renew-book-librarians'),
    # Book Edite urls.
    path('book/create/', views.BookCreate.as_view(), name= 'book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name= 'book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name= 'book-delete'),
    #_________________________________________________________________________________________
    
    
    # -------------------------------Author URLS-------------------------------
    path('authors/', views.AuthorListView.as_view(), name = 'authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name = 'author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name= 'author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name= 'author-update'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(), name= 'author-delete'),
    #_________________________________________________________________________________________
    
    
    #-------------------------------LibraryMember URLS------------------------------- 
    path('member/create/', views.Library_member_create_view, name='member-create'),
    path('members/', views.LibraryMemberListView.as_view(), name= 'member-all'),
    path('member/profile/<int:pk>', views.LibraryMemberProfile.as_view(), name= 'member-profile'),
    #_________________________________________________________________________________________
    
    
    
    
    
    
]

