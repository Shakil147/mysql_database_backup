@extends('admin.layouts.master')
@section('content')
<div class="br-pageheader">
  <nav class="breadcrumb pd-0 mg-0 tx-12">
    <a class="breadcrumb-item" href="{{ route('admin.home') }}">{{ config('app.name', 'Laravel') }}</a>
    <a class="breadcrumb-item" href="{{ route('admin.admins.index') }}">Admins</a>
    <span class="breadcrumb-item active">List</span>
  </nav>
</div><!-- br-pageheader -->
<div class="br-pagetitle">
  <i class="icon ion-ios-gear-outline"></i>
  <div>
    <h4>Admin List</h4>
    <p class="mg-b-0"></p>
  </div>
</div><!-- d-flex -->


       
      <admin-admin-list ></admin-admin-list>    


<!-- br-pagebody -->
@endsection

@push('title','Admins List')
@push('js')


@endpush
@push('css')

@endpush