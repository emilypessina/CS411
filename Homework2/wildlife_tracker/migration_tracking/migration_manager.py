from typing import Dict, List, Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:
    def __init__(self):
        self.migrations: Dict[int, Migration] = {}
        self.paths: Dict[int, MigrationPath] = {}

    def schedule_migration(self, migration_path: MigrationPath) -> None:
        pass

    def cancel_migration(self, migration_id: int) -> None:
        pass

    def get_migration_by_id(self, migration_id: int) -> Optional[Migration]:
        pass

    def get_migrations(self) -> List[Migration]:
        pass

    def get_migrations_by_status(self, status: str) -> List[Migration]:
        pass

    def get_migrations_by_current_location(self, current_location: str) -> List[Migration]:
        pass

    def get_migrations_by_migration_path(self, migration_path_id: int) -> List[Migration]:
        pass

    def get_migrations_by_start_date(self, start_date: str) -> List[Migration]:
       pass

    
    def create_migration_path(self, path_id: int, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> MigrationPath:
        pass

    def remove_migration_path(self, path_id: int) -> None:
        pass

    def get_migration_path_by_id(self, path_id: int) -> Optional[MigrationPath]:
       pass

    def get_migration_paths(self) -> List[MigrationPath]:
        pass

    def get_migration_paths_by_destination(self, destination: Habitat) -> List[MigrationPath]:
       pass
    def get_migration_paths_by_species(self, species: str) -> List[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(self, start_location: Habitat) -> List[MigrationPath]:
       pass