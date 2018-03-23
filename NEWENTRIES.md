# New Entries

## Summary Table

To make an entry into the summary table, where each column is separated by `|` and each row seperated by a new line:

* **Site**: ` [<img src="INSERT URL FOR LOGO" width="50">](INSERT WEBSITE URL)`
* **Name**:  `  [INSERT NAME HERE](#INSERT LOWERCASED NAME HERE) `
* **Category**:  `INSERT CATEGORY TEXT HERE`
* **Code**: 
  * **If Yes**:  `[<img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" width="40">](INSERT THEIR GITHUB URL HERE)`
  * **If No**: `-`
* **Demo**:
  * **If Yes and demo is a website**: `[💻][NAME-demo-site ]`
  * **If Yes and demo is a mobile app**: `[📱][NAME-demo-app ]`
  * **If No**: `-`
* **Technical Specifications (TS)**: 
  * **If Yes**: `[📃][NAME-ts)`
  * **If No**: `-`
* **Technical Specifications (TS)**: `INSERT LOCATION HERE`

At the end of the table, add the references, if they exist:
```[NAME-SECTION]: INSERT URL HERE```

For sections that you are unsure about, enter ? in the field

An example of an entry in the table:

``` 
[<img src="https://d33wubrfki0l68.cloudfront.net/9e1fb050865401a69f27b46683de38626a9372d0/9efc0/
assets/logo-color-2.png" width="50">](http://www.ambrosus.com) | [Ambrosus](#ambrosus) | 
Auditing/Supply Chain | Zug, Switzerland | [<img src="https://assets-cdn.github.com/
images/modules/logos_page/GitHub-Mark.png" width="40">][ambrosus-code] | None |
[📃][ambrosus-ts]


[ambrosus-site]:        http://ambrosus.com
[ambrosus-code]:        https://github.com/ambrosus
[ambrosus-ts]:          https://ambrosus.com/#tech-docs
[ambrosus-wp]:          https://ambrosus.com/assets/Ambrosus-White-Paper-V8-1.pdf
```


## Detailed View

Title each section 

` ## Name`

Add logo:

`[<img src="INSERT LOGO URL HERE" width="200">](INSERT WEBSITE URL)`

Add one sentence objective description:

`INSERT DESCRIPTION HERE`

Add table, fairly self explanatory. If there are multiple white papers, use a url to show all whitepapers.

```
   Details          |         -
|:-----------------:|:------------------:|
  Location          | INSERT LOCATION HERE 
  Money raised      | INSERT AMOUNT HERE
  Method of Funding | INSERT METHOD HERE
  Github Profile    | [<img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" width="40"][NAME-code]
  Dependencies      | LIST DEPENDENCIES IF ANY
  Token             | INSERT TOKEN TYPE (ERC20, ETC.)
  White Paper       | [🗒][NAME-wp]
```

You can then add references to the references from the table:

```[NAME-code]: INSERT URL FOR CODE```

```[NAME-wp]: INSERT URL FOR WHITEPAPER```

An example would be: 

```
## Ambrosus

[<img src="https://d33wubrfki0l68.cloudfront.net/9e1fb050865401a69f27b46683de38626a9372d0/9efc0/assets/logo-color-2.png" width="200">][ambrosus-site]

A blockchain for pharmaceuticals quality control
 

     Details        |        -
:------------------:|:-------------:
  Location          | Zug, Switzerland 
  Money raised      | $32 M
  Method of Funding | ICO
  Github Profile    | [<img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" width="40"][ambrosus-code]
  Dependencies      | Etheruem, IPFS
  Token             | ERC20
  White Paper       | [🗒][ambrosus-wp]
 
```


