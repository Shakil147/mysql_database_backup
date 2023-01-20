@extends('admin.layouts.master')
@section('content')

<div class="br-pageheader">
  <nav class="breadcrumb pd-0 mg-0 tx-12">
    <a class="breadcrumb-item" href="{{ route('admin.home') }}">{{ config('app.name', 'Laravel') }}</a>
    <a class="breadcrumb-item" href="{{ route('admin.admins.index') }}">Admins</a>
    <span class="breadcrumb-item active">Add</span>
  </nav>
</div><!-- br-pageheader -->
<div class="br-pagetitle">
  <i class="icon ion-ios-gear-outline"></i>
  <div>
    <h4>Admins Add</h4>
    <p class="mg-b-0"></p>
  </div>
</div><!-- d-flex -->
<admin-admin-add  :roles="{{ $roles }}"></admin-admin-add>
<!-- br-pagebody -->
@endsection

@push('title','Admin Add')
@push('js')

@endpush
@push('css')

@endpush