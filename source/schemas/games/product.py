from datetime import date, datetime
from enum import Enum
from typing import Optional, List
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel, Field, StrictStr, StrictInt, StrictBool, AnyUrl
from source.schemas.games.system_requirement import SystemRequirement, ShortSystemReqSerializers
from source.schemas.games.genre_games import GenreGames
from source.schemas.games.product_languages import ProductLanguages


class GamesList(BaseModel):
    """product list"""
    id: Optional[UUID] = Field(None, title='Id')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=100)
    releaseDate: Optional[date] = Field(None, title='Release date')
    genres: Optional[List[GenreGames]] = None
    systemRequirements: Optional[List[ShortSystemReqSerializers]] = None
    price: Optional[StrictStr] = Field(None, title='Price')
    discount: Optional[StrictInt] = Field(0, title='Discount')
    isBought: Optional[StrictBool] = Field(False, title='Is bought')
    isFavorite: Optional[StrictBool] = Field(False, title='Is favorite')


class Status(Enum):
    MODERATION = 'MODERATION'
    PUBLISH = 'PUBLISH'
    CLOSE = 'CLOSE'


class Type(Enum):
    GAMES = 'GAMES'
    DLC = 'DLC'


class Product(BaseModel):
    id: Optional[UUID] = Field(None, title='Id')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=100)
    description: StrictStr = Field(..., title='Description', min_length=1)
    developersUuid: UUID = Field(..., title='Developers uuid')
    publishersUuid: UUID = Field(..., title='Publishers uuid')
    langs: List[ProductLanguages]


class GameDetail(BaseModel):
    """product by id"""
    id: Optional[UUID] = Field(None, title='Id')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=100)
    releaseDate: Optional[date] = Field(None, title='Release date')
    genres: Optional[List[GenreGames]] = None
    price: Optional[StrictStr] = Field(None, title='Price')
    discount: Optional[StrictInt] = Field(0, title='Discount')
    isBought: Optional[StrictBool] = Field(False, title='Is bought')
    isFavorite: Optional[StrictBool] = Field(False, title='Is favorite')
    description: StrictStr = Field(..., title='Description', min_length=1)
    about: StrictStr = Field(..., title='About', min_length=1)
    age: Optional[StrictInt] = Field(None, title='Age', ge=-2147483648, le=2147483647)
    adult: Optional[StrictStr] = Field(None, title='Adult')
    status: Optional[Status] = Field(None, title='Status product')
    type: Type = Field(..., title='Type product')
    developersUuid: UUID = Field(..., title='Developers uuid')
    publishersUuid: UUID = Field(..., title='Publishers uuid')
    dlcs: List[Product]
    langs: List[ProductLanguages]
    systemRequirements: Optional[List[SystemRequirement]] = None


class Social(Enum):
    FACEBOOK = 'FACEBOOK'
    VKONTAKTE = 'VKONTAKTE'
    SITE = 'SITE'
    YOUTUBE = 'YOUTUBE'
    TWITTER = 'TWITTER'
    TWITCH = 'TWITCH'
    TELEGRAM = 'TELEGRAM'


class GameSocial(BaseModel):
    type: Optional[Social] = Field(None, title='Social_media')
    url: AnyUrl = Field(..., title='Url')


class Currency(Enum):
    RUB = 'RUB'
    USD = 'USD'
    KZT = 'KZT'
    EUR = 'EUR'


class Price(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    amount: Decimal = Field(..., title='Price')
    currency: Optional[Currency] = Field(None, title='Currency')
    createdBy: UUID = Field(..., title='Created by')
    createdAt: Optional[datetime] = Field(None, title='Created at')
    updatedBy: UUID = Field(..., title='Updated by')
    updatedAt: Optional[datetime] = Field(None, title='Updated at')


class OfferPrice(BaseModel):
    id: Optional[UUID] = Field(None, title='Id')
    price: Price
    createdBy: UUID = Field(..., title='UUID creator')
    isActive: Optional[StrictBool] = Field(None, title='Is active')
    products: Optional[List[UUID]] = Field(None, unique_items=True)


class ProductOffer(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    offer: OfferPrice
    createdBy: UUID = Field(..., title='UUID creator')
    createdAt: Optional[datetime] = Field(None, title='Created At')


class CreateProduct(BaseModel):
    """create product"""
    id: Optional[UUID] = Field(None, title='Id')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=100)
    developersUuid: UUID = Field(..., title='Developers uuid')
    publishersUuid: UUID = Field(..., title='Publishers uuid')
    description: StrictStr = Field(..., title='Description', min_length=1)
    about: StrictStr = Field(..., title='About', min_length=1)
    age: Optional[StrictInt] = Field(None, title='Age', ge=-2147483648, le=2147483647)
    adult: Optional[StrictStr] = Field(None, title='Adult')
    type: Type = Field(..., title='Type product')
    systemRequirements: List[SystemRequirement]
    langs: List[ProductLanguages]
    socials: Optional[List[GameSocial]] = None
    productOffer: ProductOffer
    genres: Optional[List[GenreGames]] = None
