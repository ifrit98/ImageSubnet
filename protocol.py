

import typing
import pydantic
import bittensor as bt
from typing import Union, TypeVar

class TextToImage( bt.Synapse ):
    images: list[ bt.Tensor ] = []
    text: str = pydantic.Field( ... , allow_mutation = False)
    height: int = pydantic.Field( 512 , allow_mutation = False)
    width: int = pydantic.Field( 512 , allow_mutation = False)
    num_images_per_prompt: int = pydantic.Field( 1 , allow_mutation = False)
    num_inference_steps: int = 20
    guidance_scale: float = 7.5
    negative_prompt: str = pydantic.Field( ... , allow_mutation = False)
    seed: int = pydantic.Field( -1 , allow_mutation = False)

class ImageToImage( TextToImage ):
    image: bt.Tensor = pydantic.Field( ... , allow_mutation = False)
    strength: float = pydantic.Field( 1.0 , allow_mutation = False)

T = TypeVar('T', bound=Union[TextToImage, ImageToImage])