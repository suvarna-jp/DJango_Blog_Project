from django.shortcuts import render
from django.http import HttpResponse

productscatalog = [ 
    {
        'categoryname' : 'Diyas',
        'products' : [
            {
                'productname' : 'Ganesh Diya',
                'imagepath' : 'Blog Post abc',
                'color' : 'Orange',
                'price' : u'\u20B9 200',
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            },
            {
                'productname' : 'Saraswathi Diya',
                'imagepath' : 'Blog Post abc',
                'color' : 'White',
                'price' : u"\u20B9 150",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            },
            {
                'productname' : 'Lakshmi Diya',
                'imagepath' : 'Blog Post abc',
                'color' : 'Red',
                'price' : 	u"\u20B9 300",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            }
        ]
    },
    {
        'categoryname' : 'Kumkum Boxes',
        'products' : [
            {
                'productname' : 'Rose Kumkum Box',
                'imagepath' : 'Blog Post abc',
                'color' : 'White',
                'price' : u"\u20B9 150",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            },
            {
                'productname' : 'Conch Shaped Kumkum Box',
                'imagepath' : 'Blog Post abc',
                'color' : 'Red',
                'price' : 	u"\u20B9 300",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            }
        ]
    },
    {
        'categoryname' : 'OHP Rangoli',
        'products' : [
            {
                'productname' : 'Diya Shaped Rangoli',
                'imagepath' : 'Blog Post abc',
                'color' : 'White',
                'price' : u"\u20B9 150",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            },
            {
                'productname' : 'Geometrical Shapes Rangoli',
                'imagepath' : 'Blog Post abc',
                'color' : 'Red',
                'price' : 	u"\u20B9 300",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            }
        ]
    },
    {
        'categoryname' : 'Lamps',
        'products' : [
            {
                'productname' : 'Bottle light lamps',
                'imagepath' : 'Blog Post abc',
                'color' : 'White',
                'price' : u"\u20B9 150",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'October 30th, 2019',
            },
            {
                'productname' : 'Peacock Artwork Lamps',
                'imagepath' : 'Blog Post abc',
                'color' : 'Red',
                'price' : 	u"\u20B9 300",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'January 20th, 2020',
            },
            {
                'productname' : 'Wall Mounted Lamps',
                'imagepath' : 'Blog Post abc',
                'color' : 'White',
                'price' : u"\u20B9 150",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'December 15th, 2019',
            },
            {
                'productname' : 'Thread-Art Lamps',
                'imagepath' : 'Blog Post abc',
                'color' : 'Red',
                'price' : 	u"\u20B9 300",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'November 30th, 2019',
            }
        ]
    },
    {
        'categoryname' : 'Decoratives',
        'products' : [
            {
                'productname' : 'Wall Mounted Lamps',
                'imagepath' : 'Blog Post abc',
                'color' : 'White',
                'price' : u"\u20B9 150",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'December 15th, 2019',
            },
            {
                'productname' : 'Thread-Art Lamps',
                'imagepath' : 'Blog Post abc',
                'color' : 'Red',
                'price' : 	u"\u20B9 300",
                'date_posted' : 'October 6th, 2019',
                'stockavailability' : 6,
                'stockavailability_startdate' : 'October 10th, 2019',
                'stockavailability_enddate' : 'November 30th, 2019',
            }
        ]
    }
]

def home(request):
    context = {
        'productscatalog' : productscatalog
    }
    return render(request, 'bloggers_adda/home.html', context)

def about(request):
    return render(request, 'bloggers_adda/about.html')
