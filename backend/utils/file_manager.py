import os
import json
import pickle

class FileManager:

  # DIRECTORIES METHODS -------------------------------------------------

  def create_directory(self,
                       dirs: str | list[str],
                       mode: str = "single"
                       ) -> dict | list[dict]:

    def _create(path_: str) -> dict:
      msg = {"path": path_, "status": None}

      if self.validate_directory(path=path_):
        try:
          os.mkdir(path_)
          msg["status"] = "created"

        except Exception as e:
          msg["status"] = f"failed. error: {str(e)}"
      else:
        msg["status"] = "already exists"

      return msg

    if mode == "multiple":
      msgs = [_create(path_=path) for path in dirs]
      return msgs

    return _create(path_=dirs)

  @staticmethod
  def validate_directory(path: str) -> bool:
    return not os.path.exists(path=path)

  # JSON METHODS -------------------------------------------------

  @staticmethod
  def read_json(path: str):
    with open(path, "w") as json_file:
      return json.load(json_file)

  @staticmethod
  def save_json(path: str, object_) -> None:
    with open(path, "w") as json_file:
      json.dump(object_, json_file, indent=2)

# PICKLE METHODS -------------------------------------------------

  @staticmethod
  def read_pickle(path: str):
    with open(path, "rb") as f:
      return pickle.load(f)

  @staticmethod
  def save_pickle(path: str, object_) -> None:
    with open(path, "wb") as f:
      pickle.dump(object_, f)