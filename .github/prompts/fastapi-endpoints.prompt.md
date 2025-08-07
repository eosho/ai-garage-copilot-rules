---
description: "Generate a complete FastAPI router with CRUD endpoints for a resource."
mode: "ask"
---

# FastAPI CRUD Endpoint Generation

Please generate a complete FastAPI router with full CRUD (Create, Read, Update, Delete) functionality for the `${resource_name_pascal_case}` resource.

The implementation should strictly follow our project's standards for security, data validation, and architecture.

## Resource Details

- **Resource Name (PascalCase)**: `${resource_name_pascal_case}`
- **Resource Name (snake_case)**: `${resource_name_snake_case}`
- **Plural Resource Name (snake_case)**: `${resource_name_plural_snake_case}`
- **Primary Key Type**: `${pk_type:int}`

## Instructions

1.  **Pydantic Schemas**:

    - Create ` ${resource_name_pascal_case}Base`, `${resource_name_pascal_case}Create`, `${resource_name_pascal_case}Update`, and `${resource_name_pascal_case}Response` schemas.
    - Apply validation rules as defined in our [Pydantic Models Instructions](./pydantic-models.md).

2.  **Service Layer**:

    - Assume a `services/${resource_name_snake_case}_service.py` exists with a `${resource_name_pascal_case}Service` class.
    - This service should have methods for `create_${resource_name_snake_case}`, `get_${resource_name_snake_case}_by_id`, `get_all_${resource_name_plural_snake_case}`, `update_${resource_name_snake_case}`, and `delete_${resource_name_snake_case}`.

3.  **API Router**:

    - Create a new router in `routers/${resource_name_snake_case}.py`.
    - The router prefix should be `/api/v1/${resource_name_plural_snake_case}`.
    - Implement endpoints for all five CRUD operations (Create, Get One, Get All, Update, Delete).

4.  **Dependencies and Security**:

    - Inject the database session (`db: Session = Depends(get_db)`).
    - Inject the service layer (`service: ${resource_name_pascal_case}Service = Depends()`).
    - Secure all endpoints that modify data using an authentication dependency (`current_user: User = Depends(get_current_active_user)`).
    - Follow all guidelines from our [Security-First Instructions](../instructions/shared/security-first.instructions.md).

5.  **Error Handling**:
    - Implement robust error handling.
    - Raise `HTTPException` with appropriate status codes (e.g., 404 for not found, 400 for bad requests).

## Example Code Structure

Please generate the code for the `routers/${resource_name_snake_case}.py` file, following this structure:

```python
# routers/{resource_name_snake_case}.py

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_active_user
from ..schemas.${resource_name_snake_case} import ${resource_name_pascal_case}Create, ${resource_name_pascal_case}Update, ${resource_name_pascal_case}Response
from ..services.${resource_name_snake_case}_service import ${resource_name_pascal_case}Service
from ..models.user import User

router = APIRouter(
    prefix="/api/v1/${resource_name_plural_snake_case}",
    tags=["${resource_name_pascal_case}"],
    responses={404: {"description": "Not found"}},
)

# --- CRUD Endpoints ---

@router.post("/", response_model=${resource_name_pascal_case}Response, status_code=status.HTTP_201_CREATED)
def create_${resource_name_snake_case}(
    ${resource_name_snake_case}_in: ${resource_name_pascal_case}Create,
    db: Session = Depends(get_db),
    service: ${resource_name_pascal_case}Service = Depends(),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new ${resource_name_snake_case}.
    """
    return service.create_${resource_name_snake_case}(db=db, obj_in=${resource_name_snake_case}_in)

@router.get("/", response_model=List[${resource_name_pascal_case}Response])
def read_${resource_name_plural_snake_case}(
    db: Session = Depends(get_db),
    service: ${resource_name_pascal_case}Service = Depends(),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve all ${resource_name_plural_snake_case}.
    """
    return service.get_all_${resource_name_plural_snake_case}(db=db, skip=skip, limit=limit)

@router.get("/{${resource_name_snake_case}_id}", response_model=${resource_name_pascal_case}Response)
def read_${resource_name_snake_case}(
    ${resource_name_snake_case}_id: ${pk_type},
    db: Session = Depends(get_db),
    service: ${resource_name_pascal_case}Service = Depends()
):
    """
    Get a specific ${resource_name_snake_case} by ID.
    """
    db_${resource_name_snake_case} = service.get_${resource_name_snake_case}_by_id(db=db, id=${resource_name_snake_case}_id)
    if db_${resource_name_snake_case} is None:
        raise HTTPException(status_code=404, detail="${resource_name_pascal_case} not found")
    return db_${resource_name_snake_case}

@router.put("/{${resource_name_snake_case}_id}", response_model=${resource_name_pascal_case}Response)
def update_${resource_name_snake_case}(
    ${resource_name_snake_case}_id: ${pk_type},
    ${resource_name_snake_case}_in: ${resource_name_pascal_case}Update,
    db: Session = Depends(get_db),
    service: ${resource_name_pascal_case}Service = Depends(),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a ${resource_name_snake_case}.
    """
    db_${resource_name_snake_case} = service.get_${resource_name_snake_case}_by_id(db=db, id=${resource_name_snake_case}_id)
    if db_${resource_name_snake_case} is None:
        raise HTTPException(status_code=404, detail="${resource_name_pascal_case} not found")
    return service.update_${resource_name_snake_case}(db=db, db_obj=db_${resource_name_snake_case}, obj_in=${resource_name_snake_case}_in)

@router.delete("/{${resource_name_snake_case}_id}", response_model=${resource_name_pascal_case}Response)
def delete_${resource_name_snake_case}(
    ${resource_name_snake_case}_id: ${pk_type},
    db: Session = Depends(get_db),
    service: ${resource_name_pascal_case}Service = Depends(),
    current_user: User = Depends(get_current_active_user)
):
    """
    Delete a ${resource_name_snake_case}.
    """
    db_${resource_name_snake_case} = service.get_${resource_name_snake_case}_by_id(db=db, id=${resource_name_snake_case}_id)
    if db_${resource_name_snake_case} is None:
        raise HTTPException(status_code=404, detail="${resource_name_pascal_case} not found")
    return service.delete_${resource_name_snake_case}(db=db, id=${resource_name_snake_case}_id)
```
