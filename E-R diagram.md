```mermaid
erDiagram
    User {
        int id PK
        string username
        string password
        string name
        string postcode
        string roadaddress
        string jibunaddress
        string detailaddress
    }
    Article {
        int id PK
        int author_id FK
        string title
        text content
        datetime created_at
        datetime updated_at
    }
    Comment {
        int id PK
        int article_id FK
        int author_id FK
        text content
        datetime created_at
        datetime updated_at
    }
    DepositProductsBaseInfo {
        int base_product_id PK
        string fin_co_no
        string kor_co_nm
        string fin_prdt_cd
        string fin_prdt_nm
        string join_way
        text mtrt_int
        text spcl_cnd
        string join_deny
        string join_member
        string etc_note
        int max_limit
        string dcls_strt_day
        string dcls_end_day
        string fin_co_subm_day
    }
    DepositProductsOption {
        int id PK
        int base_product_id FK
        string fin_co_no
        string fin_prdt_cd
        string intr_rate_type
        string intr_rate_type_nm
        string save_trm
        decimal intr_rate
        decimal intr_rate2
    }
    FixedSavingProductsBaseInfo {
        int base_product_id PK
        string fin_co_no
        string kor_co_nm
        string fin_prdt_cd
        string fin_prdt_nm
        string join_way
        text mtrt_int
        text spcl_cnd
        string join_deny
        string join_member
        string etc_note
        int max_limit
        string dcls_strt_day
        string dcls_end_day
        string fin_co_subm_day
    }
    FixedSavingProductsOption {
        int id PK
        int base_product_id FK
        string fin_co_no
        string fin_prdt_cd
        string intr_rate_type
        string intr_rate_type_nm
        string save_trm
        decimal intr_rate
        decimal intr_rate2
    }
    FreeSavingProductsBaseInfo {
        int base_product_id PK
        string fin_co_no
        string kor_co_nm
        string fin_prdt_cd
        string fin_prdt_nm
        string join_way
        text mtrt_int
        text spcl_cnd
        string join_deny
        string join_member
        string etc_note
        int max_limit
        string dcls_strt_day
        string dcls_end_day
        string fin_co_subm_day
    }
    FreeSavingProductsOption {
        int id PK
        int base_product_id FK
        string fin_co_no
        string fin_prdt_cd
        string intr_rate_type
        string intr_rate_type_nm
        string save_trm
        decimal intr_rate
        decimal intr_rate2
    }

    User ||--o{ Article : writes
    Article ||--o{ Comment : receives
    User ||--o{ Comment : writes

    User ||--o{ DepositProductsBaseInfo : likes
    User ||--o{ FixedSavingProductsBaseInfo : likes
    User ||--o{ FreeSavingProductsBaseInfo : likes

    DepositProductsBaseInfo ||--o{ User : liked_by
    FixedSavingProductsBaseInfo ||--o{ User : liked_by
    FreeSavingProductsBaseInfo ||--o{ User : liked_by

    DepositProductsBaseInfo ||--|{ DepositProductsOption : has_option
    FixedSavingProductsBaseInfo ||--|{ FixedSavingProductsOption : has_option
    FreeSavingProductsBaseInfo ||--|{ FreeSavingProductsOption : has_option