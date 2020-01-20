# Get products by UserID with totalCount
```
query {
    productsByuser {   
    totalCount
    edges {      
      node {                
        title
        userid
        {
            id
        }
      }
    }
  }
}
```
#Products get
```
query GET_PRODUCTS {
  products {
    edges {
      node {
        productid
        category: categoryid {
          categoryid
          title
        }
        title
        description
        user: userid {
          id
          username
        }
        created
      }
    }
    pageInfo{
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}
```

# Get products with totalCount
```
query {
    products {   
    totalCount
    edges {      
      node {                
        title
        userid
        {
            id
        }
      }
    }
  }
}
```

# Product get by id
```
query GET_PRODUCT($productid: Int!) {
  product(productid: $productid) {
    productid
    category: categoryid {
      categoryid
      title
    }
    title
    description
    user: userid {
      id
      username
    }
    created
  }
}
```
# Product get by id variables
```
{
  "productid": 13
}
```
# Product create
```
mutation CREATE_PRODUCT
(
  $categoryid: Int!,
  $title: String!,
  $description: String
)
{
  createProduct 
  (
  	categoryid: $categoryid,
    title: $title,
    description: $description
  )
  {
    product {
      productid
      category: categoryid {
        categoryid
        title
      }
      title
      description
      created
    }
  }
}
```

# Get products total count 
```
query {
    products {   
    	totalCount
    }
}
```
# Product create variables
```
{
  "categoryid": 3,
  "title": "Product New",
  "description": "Product New description"
}
```


# Product update
```
mutation UPDATE_PRODUCT
(
  $productid: Int!,
  $categoryid: Int!,
  $title: String!,
  $description: String
)
{
  updateProduct 
  (
    productid: $productid,
  	categoryid: $categoryid,
    title: $title,
    description: $description
  )
  {
    product {
      productid
      category: categoryid {
        categoryid
        title
      }
      title
      description
      created
    }
  }
}
```
# Product update variables
```
{
  "productid": 13,
  "categoryid": 2,
  "title": "Product 2 Updated",
  "description": "Product 2 description"
}
```

# Get products by category title
```
query getProductsByCategoryTitle($category_title: String){
  productsBycategoryTitle(categoryTitle: $category_title){    
    edges{
      node{       
        title
        categoryid{
          categoryid
          title
        }
      }
    }
  }
}
```

# Variable get products by category title
```
{
  "category_title": "def"
}
```

# Get products by UserID and (optional) by CategoryID
```
query getProductsByUserID($category_title: String){
  productsByuser(categoryTitle: $category_title){    
    edges{
      node{
        title
        userid{
          id
        }
        categoryid{
          categoryid
          title
        }
      }
    }
  }
}
```

# Variable get products by UserID and (optional) by CategoryID
```
{
  "category_title": "categ"
}
```